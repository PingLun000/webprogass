 
from django.http import request
from django.urls import path,include
from . import views



app_name='members'

urlpatterns=[
   
    #https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication
    path('login/',include('django.contrib.auth.urls')),#,namespace='signIn'
    path('logout/',include('django.contrib.auth.urls')),
    #path('signIn/',views.signIn, name='signIn'),
    path('register/',views.register, name='register'),
      
    
]