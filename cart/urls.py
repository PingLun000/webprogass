from django.urls import path
from .import views

 
app_name='cart'

urlpatterns=[
    path('', views.carts,name='carts'),
    path('addToCart/<int:product_id>/',views.addToCart,name='addToCart'),
    path('removeFromCart/<int:product_id>/',views.removeFromCart,name='removeFromCart'),
    path('deleteFromCart/<int:product_id>/',views.deleteFromCart,name='deleteFromCart'),
]