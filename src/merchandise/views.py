from django.db.models import Sum

from order.models import Order
from merchandise.models import Product

from merchandise.serializers import ProductSerializer

from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class ProductView(GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @swagger_auto_schema(
        operation_summary = 'mer-01-get 查詢商品列表',
        manual_parameters = [
            openapi.Parameter(
                'top',
                in_ = openapi.IN_QUERY,
                description = '是否得到銷售前 3 名',
                type = openapi.TYPE_BOOLEAN,
                default = False
            )
        ]
    )
    def get(self, request):
        products = self.get_queryset().order_by('product_id')
        
        if request.GET.get('top') == 'true':
            top_product_ids = list(Order.objects.values_list('product_id', flat = True).annotate(total = Sum('qty'))[:3])
            products = products.filter(product_id__in = top_product_ids)
            
        if products:
            serializer = self.serializer_class(products, many = True)
            data = serializer.data
            return Response(data = data, status = status.HTTP_200_OK)
        return Response(data = [], status = status.HTTP_200_OK)
    
    
