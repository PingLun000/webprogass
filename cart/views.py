from django.core.exceptions import ObjectDoesNotExist
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from store.models import Product
from .models import Cart, CartProduct
from django.contrib.auth.decorators import login_required

# Create your views here.


def cartID(request):
    cart=request.session.session_key
    if not cart:
        cart=request.session.create()
    return cart    
        
 
def addToCart(request,product_id):
    product=Product.objects.get(id=product_id)#get the product
    try:
        cart=Cart.objects.get(cart_ID=cartID(request)) # get the cart using cartID using session 
    except Cart.DoesNotExist:
        cart=Cart.objects.create(
            cart_ID=cartID(request)
        )    
    cart.save()
    
    try:
        cart_product=CartProduct.objects.get(product=product,cart=cart)
        cart_product.quantiy+=1 # card_item quantiy
        cart_product.save()
    except CartProduct.DoesNotExist:
        cart_product=CartProduct.objects.create(
            product=product,
            quantiy=1,
            cart=cart,
        )
        cart_product.save()
  
    return redirect('cart:carts')


def removeFromCart(request,product_id):
    product=Product.objects.get(id=product_id)#get the product
    cart=Cart.objects.get(cart_ID=cartID(request)) # get the cart using cartID using session 
    cart_product=CartProduct.objects.get(product=product,cart=cart)
    
    
    if cart_product.quantiy>1:
        cart_product.quantiy-=1 # card_item quantiy
        cart_product.save()
    else:
        cart_product.delete()
           
    return redirect('cart:carts')


def deleteFromCart(request,product_id):
    
    product=Product.objects.get(id=product_id)#get the product
    cart=Cart.objects.get(cart_ID=cartID(request)) # get the cart using cartID using session 
    cart_product=CartProduct.objects.get(product=product,cart=cart)
    cart_product.delete()
    
    return redirect('cart:carts')
    
    
def carts(request,total=0,quantiy=0,discount=0,payable=0,cart_product=None):

    try:
        carts=Cart.objects.get(cart_ID=cartID(request))
        cart_products=CartProduct.objects.filter(cart=carts)
        for cart_product in cart_products:
            total=total+(cart_product.product.price*cart_product.quantiy)
            discount=discount +(cart_product.product.discount*cart_product.quantiy)
            quantiy+=cart_product.quantiy
            payable=total-discount
    except ObjectDoesNotExist:
        pass
    
    context={
        'discount':discount,
        'total': total,
        'quantiy': quantiy,
        'cart_products':cart_products,
        'payable':payable,

    }        
    return render(request,'cart.html',context)



