from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import BooleanField, FloatField
from django.db.models.fields.related import ForeignKey

from store.models import Product
 

# Create your models here.

'''class Order(models.Model):
    member=Model.ForeignKey(members,on_delete=models.CASCADE)
    Order_product=models.BooleanField(default=False)
    total_price=models.FloatField(default=0)
    
    def __str__(self):
        return self.cart_ID'''
    
class Cart(models.Model):
    cart_ID=models.CharField(max_length=255,blank=True)
    date_added=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.cart_ID
    
class CartProduct(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantiy=models.IntegerField()
    created=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.product
    
    def total_price(self):
        return self.quantiy*self.product.price 
    
     
     