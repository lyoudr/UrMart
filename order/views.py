from django.db import transaction

from order.models import Order
from order.serializers import OrderSerializer
from merchandise.models import Product

from product.custom_res import CustomError
from product.decorators import check_vip_stock


from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class OrderView(GenericAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    stock_avl = True

    @swagger_auto_schema(
        operation_summary = 'order-01-get 取得訂單',
        manual_parameters = [
            openapi.Parameter(
                'establish',
                in_ = openapi.IN_QUERY,
                description = 'all:全部 0: 不成立 1: 成立 (必填)',
                type = openapi.TYPE_STRING,
                required = True,
                default = '1'
            ),
            openapi.Parameter(
                'customer_id',
                in_ = openapi.IN_QUERY,
                description = '客戶 id (非必填)',
                type = openapi.TYPE_INTEGER,
                default = 1
            )
        ]
    )
    def get(self, request):
        if not request.GET.get('establish'):
            raise CustomError(
                return_code = 'mer-01-get_not-fill-required-field',
                return_message = 'not fill required field establish',
                status_code = status.HTTP_400_BAD_REQUEST,
            )
        condition = {
            'establish': request.GET.get('establish') if request.GET.get('establish') in ('0', '1') else None,
            'customer_id': request.GET.get('customer_id')
        }
        orders = self.queryset.filter(**{key:val for key, val in condition.items() if val}).order_by('id')
        
        if orders:
            serializer = self.serializer_class(orders, many = True)
            data = serializer.data
            return Response(data = data, status = status.HTTP_200_OK)
        return Response(data = [], status = status.HTTP_200_OK)


    @swagger_auto_schema(
        operation_summary = 'order-02-post 將商品新增至訂單',
        request_body = openapi.Schema(
            type = openapi.TYPE_OBJECT,
            properties = {
                'product_id': openapi.Schema(
                    type = openapi.TYPE_STRING,
                    description = '商品 id',
                    example = 1
                ),
                'price' : openapi.Schema(
                   type = openapi.TYPE_INTEGER,
                   description = '商品單價',
                   example = 100
                ),
                'qty': openapi.Schema(
                    type = openapi.TYPE_INTEGER,
                    description = '購買數量',
                    example = 3
                ),
                'shop_id': openapi.Schema(
                    type = openapi.TYPE_STRING,
                    description = '商品所屬館別 id',
                    example = 'ps',
                ),
                'customer_id': openapi.Schema(
                    type = openapi.TYPE_INTEGER,
                    description = '客戶 id',
                    example = 1,
                )
            }
        )
    )
    @check_vip_stock()
    def post(self, request):
        data = request.data
        with transaction.atomic():
            data['establish'] = '0' 

            # update product stock if stock is available
            if self.stock_avl:
                product = Product.objects.get(pk = data.get('product_id'))
                product.stock_pcs = product.stock_pcs - data.get('qty')
                product.save()
                data['establish'] = '1'
            
            # update order
            data.update({'price': data.get('price') * data.get('qty')})

            serializer = self.serializer_class(data = data)
            serializer.is_valid(raise_exception = True)
            serializer.save()

            resp = self.serializer_class(self.get_queryset(), many = True).data
            return Response(data = resp, status = status.HTTP_200_OK)


class OrderDeleteView(GenericAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @swagger_auto_schema(
        operation_summary = 'order-02-delete 刪除訂單',
    )
    def delete(self, request, pk):
        with transaction.atomic():
            try :
                order = self.queryset.get(pk = pk)
                product = Product.objects.get(product_id = order.product_id)
            except :
                raise CustomError(
                    return_code = 'order-02-delete_not-found',
                    return_message = 'order or product is not found',
                    status_code = status.HTTP_404_NOT_FOUND 
                )
            # update product stock
            if order.establish == '1':
                product.stock_pcs = product.stock_pcs + order.qty
                product.save()

            # delete order
            order.delete()
            orders = self.get_queryset()
            serializer = self.serializer_class(orders, many = True)
            data = serializer.data
        
        return Response(data = data, status = status.HTTP_200_OK)