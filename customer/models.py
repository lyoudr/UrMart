from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser

class Customer(AbstractBaseUser):
    class Meta:
        db_table = 'CUSTOMER'
    
    user_name = models.CharField(max_length = 100)
    vip = models.BooleanField(default = True)
    
    def __str__(self):
        return self.user_name

    
