from django.shortcuts import render
from django.urls.conf import path
from django.urls.resolvers import URLPattern
from . import views
# Create your views here.


app_name='store'

urlpatterns=[
    
      path('view/',views.storeProducts, name='storeProducts'),
      path('',views.storeProducts, name='storeProducts'),
      #<slug refers to datatype want to store and pass :
      # /item/chef-weslen/
      path('item/<slug:slug>/',views.productDetail, name='productDetail'),
      #/private-chef/ category
      path('<slug:category_slug>/',views.main, name='products_by_category'),
    
    
]