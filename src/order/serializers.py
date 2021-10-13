from order.models import Order
from rest_framework import serializers

class OrderSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField()
    shop_id = serializers.CharField()
    customer_id = serializers.IntegerField()
    establish = serializers.CharField()
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