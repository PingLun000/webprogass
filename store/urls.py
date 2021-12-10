from django.shortcuts import render
from django.urls.conf import path
from django.urls.resolvers import URLPattern
from . import views
# Create your views here.


app_name='store'

urlpatterns=[
    
      path('',views.storeProducts, name='storeProducts'),
       
      #<slug refers to datatype want to stored and pass :
      # /item/chef-weslen/
      path('product/<slug:slug>/',views.productDetail, name='productDetail'),
     
      path('category/<slug:category_slug>/',views.productCategory, name='productCategory'),
      
      path('search/', views.searchResult, name='searchResult')
    
]