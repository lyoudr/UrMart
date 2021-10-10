from django.db import models

class Shop(models.Model):
    class Meta:
        db_table = 'SHOP'
    
    shop_id = models.CharField(primary_key = True , max_length = 10)
    shop_name = models.CharField(max_length = 50, null = True)

    def __str__(self):
        return self.shop_id