from .models import Cart,CartProduct
from .views import cartID


def count(request):
    cart_productNo=0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart = Cart.objects.filter(cart_ID=cartID(request))
            
            cart_products = CartProduct.objects.all().filter(cart=cart[:1])
                
            for cart_no in cart_products:
                cart_productNo =cart_productNo+cart_no.quantiy
        except Cart.DoesNotExist:
            cart_count = 0
    return dict(cart_productNo=cart_productNo)
