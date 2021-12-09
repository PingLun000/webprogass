 
from django.http import request
from django.urls import path,include
from . import views



app_name='members'

urlpatterns=[
   
    path('login/',include('django.contrib.auth.urls')),#,namespace='signIn'
    #path('signIn/',views.signIn, name='signIn'),
    path('register/',views.register, name='register'),
    
]