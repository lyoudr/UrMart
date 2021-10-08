from django.db.models import Sum

from merchandise.models import Product
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    sell_qty = serializers.SerializerMethodField()

    def get_sell_qty(self, instance):
        qty = instance.order_a.aggregate(Sum('qty')).get('qty__sum')
        return qty if qty else 0
        


    class Meta:
        model = Product
        fields = ('product_id', 'stock_pcs', 'price', 'shop', 'vip', 'sell_qty')