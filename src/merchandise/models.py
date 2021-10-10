from django.db import models

from shop.models import Shop

class Product(models.Model):
    class Meta:
        db_table = 'PRODUCT'

    product_id = models.AutoField(primary_key = True)
    stock_pcs = models.IntegerField(default = 1)
    price = models.IntegerField()
    shop = models.ForeignKey(Shop, on_delete = models.CASCADE, related_name = 'product')
    vip = models.BooleanField(default = True)

    def __str__(self):
        return f'{self.product_id}'
