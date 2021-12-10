from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import BooleanField, FloatField
from django.db.models.fields.related import ForeignKey

from .models import members,Product
 

# Create your models here.

class Cart(models.Model):
    member=Model.ForeignKey(members,on_delete=models.CASCADE)
    Order_product=models.BooleanField(default=False)
    total_price=models.FloatField(default=0)
    
class CartItem(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    price=models.FloatField(default=0)
    total_items=models.IntegerField(default=0)
    quantiy=models.IntegerField(default=1)
    created=models.DateTimeField(auto_now_add=True)
