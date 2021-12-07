from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class Category(models.Model):
    category_name=models.CharField(max_length=255,unique=True)
    #url of category slug field cant accept any special charactor
    slug =models.SlugField(max_length=100,unique=True)
    description=models.TextField(max_length=255,blank=True)
    #where you upload to
    cart_image=models.ImageField(upload_to='image/categories',blank=True)
    
    #data about data, used to correct the name given
    class Meta:
        verbose_name='category'
        #change the name in admin page because itj ust simply add s behind category
        verbose_name_plural='categories'
        
    def getProductCategory(self):
            #the store is the app name defined in urls, detail is the name given in path
        # refer back to the unique items as slug
        # this line is use to reverse the specific link back 
        return reverse('store:productCategory',args=[self.slug])   
        
    def __str__(self):
        return self.category_name
    

# Create your models here.
class Product(models.Model): 
    #used as a FK to retrieve data from Category Table
    category_name=models.ForeignKey(Category,related_name='product',on_delete=models.CASCADE)  
    #pre-defined by django in line 3, for User 
    created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='product_creator')
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=255,default='admin')
    description=models.TextField(blank=True)
    #image/ = path
    image=models.ImageField(upload_to='image/products')
    slug=models.SlugField(max_length=255)
    price=models.DecimalField(max_digits=8,decimal_places=2)
    in_stock=models.BooleanField(default=True)
    is_active=models.BooleanField(default=True)
    updated =models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        #-created's -means ordering by the last added items asc/desc
        ordering=('-created',)
    
    def getProductDetail(self):
        #the store is the app name defined in urls, detail is the name given in path
        # refer back to the unique items as slug
        # this line is use to reverse the specific link back 
        return reverse('store:productDetail',args=[self.slug])   
     
    def __str__(self):
        return self.title 