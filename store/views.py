 
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
    product=get_object_or_404(Product,slug=slug,in_stock=True)
    return render(request,'productDetail.html',{'product':product})

def productCategory(request,category_slug):
    category=get_object_or_404(Category,slug=category_slug)
    products=Product.objects.filter(category_name=category)
    return render(request, 'category.html',{'category':category,'products':products})

def searchResult(request):
    if request.method=="POST":
        # retrieve it from front-end and pass it to .html
        find=request.POST['find']
        items=Product.objects.filter(title__contains=find,is_active=True,in_stock=True)
        return render(request,'searchResult.html',{'searched':find,'items':items})
    else:
        return render(request,'searchResult.html',{})