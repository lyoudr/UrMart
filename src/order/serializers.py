from order.models import Order
from rest_framework import serializers

class OrderSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField()
    shop_id = serializers.CharField()
    customer_id = serializers.IntegerField()
    establish = serializers.CharField()

    # def create(self, data):
    #     try : 
    #         order = Order.objects.get(
    #             product_id = data.get('product_id'), 
    #             shop_id = data.get('shop_id')
    #         )
    #         for key, value in data.items():
    #             if key == 'qty':
    #                 value = order.qty + data.get('qty')
    #                 print('value is =>', value)
    #             setattr(order, key, value)
    #         order.save()
    #     except Order.DoesNotExist:
    #         print('here')
    #         order = Order(**data)
    #         order.save()
        
        # return order

        
    class Meta:
        model = Order
        fields = (
            'id',
            'product_id',
            'qty',
            'price',
            'shop_id',
            'customer_id',
            'establish',
        )