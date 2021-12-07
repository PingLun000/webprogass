 
from django.shortcuts import get_object_or_404, render
from .models import Product,Category

# Create your views here.

def categories(request):
    return{
        'categories':Category.objects.all()
    }

def storeProducts(request):
    #running a query on product table 
    products=Product.objects.all()
    return render(request,'home.html',{'products':products})

def productDetail(request,slug):
    product=get_object_or_404(Product,slug=slug,in_stock=True,is_active=True)
    return render(request,'productDetail.html',{'product':product})
    
#change it to category 
def main(request,category_slug=None):
    categories =None
    products=None
    
    if category_slug!=None:
        categories=get_object_or_404(Category,slug=category_slug)
        products=Product.objects.filter(category_name=categories,is_active=True)
        product_count=products.count()
    else    :
        #categories=get_object_or_404(Category,category_slug=slug)
        products=Product.objects.filter(category_name=categories,is_active=True)
        product_count=products.count()
        
        
    products=Product.objects.all().filter(is_active=True)
    
    return render (request,'home.html',{'products':products}) 