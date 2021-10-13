from django.db.models import Sum

from merchandise.models import Product
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('product_id', 'stock_pcs', 'price', 'shop', 'vip', 'sell_qty')