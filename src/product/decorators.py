from customer.models import Customer
from merchandise.models import Product

from product.custom_res import CustomError

from rest_framework import status

def check_vip_stock():
    def decorator(func):
        def decorated_func(self, *args, **kwargs):
            data = self.request.data
            if not data.get('qty') or not data.get('customer_id') or not data.get('product_id'):
                raise CustomError(
                    return_code = 'not fill qty or customer_id or product_id',
                    return_message = 'not fill qty or customer_id or product_id',
                    status_code = status.HTTP_404_NOT_FOUND,
                )
            try :
                user = Customer.objects.get(pk = data.get('customer_id'))
                product = Product.objects.get(pk = data.get('product_id'))
            except Customer.DoesNotExist:
                raise CustomError(
                    return_code = 'order-02-post_not-found',
                    return_message = 'customer is not found',
                    status_code = status.HTTP_404_NOT_FOUND,
                )
            except Product.DoesNotExist:
                raise CustomError(
                    return_code = 'order-02-post_not-found',
                    return_message = 'product is not found',
                    status_code = status.HTTP_404_NOT_FOUND,
                )
            user_is_vip = user.vip
            prod_is_vip = product.vip
            # check vip
            if prod_is_vip and not user_is_vip:
                raise CustomError(
                    return_code = 'order-02-post_common-error',
                    return_message = 'user is not vip, can not buy this product',
                    status_code = status.HTTP_400_BAD_REQUEST
                )
            # check stock available
            self.stock_avl = product.stock_pcs >= data.get('qty')
            
            return func(self, *args, **kwargs)
        return decorated_func
    return decorator