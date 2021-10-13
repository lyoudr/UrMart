from django.db import models
from django.db.models import Sum

from merchandise.models import Product
from shop.models import Shop
from customer.models import Customer

class Order(models.Model):
    class Meta:
        db_table = 'ORDER'
    
    ESTABLISTH_CHOICES = (
        ('0', '不成立'),
        ('1', '成立')
    )
    product = models.ForeignKey(Product, on_delete = models.CASCADE, related_name = 'order_a')
    qty = models.IntegerField(default = 1)
    price = models.IntegerField()
    shop = models.ForeignKey(Shop, on_delete = models.CASCADE, related_name = 'order_b')
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE, related_name = 'order_c', null = True)
    establish = models.CharField(max_length = 1, choices = ESTABLISTH_CHOICES, default = '1')

    def __str__(self):
        return f'{self.id}-{self.product.product_id}'
    
    @classmethod
    def top_thr(self):
        return list(self.objects.values_list('product_id', flat = True).annotate(total = Sum('qty'))[:3])