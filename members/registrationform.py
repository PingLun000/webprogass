
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class registerationForm(UserCreationForm):
    
    #check here https://dev.to/yahaya_hk/usercreation-form-with-multiple-fields-in-django-ek9
    first_name = forms.CharField()
    last_name = forms.CharField()
    contact_number=forms.CharField()
    email=forms.EmailField()
    
    #used to store in parent class(User's) database 
    class Meta:
       #https://docs.djangoproject.com/en/1.8/_modules/django/contrib/auth/forms/
        model=User
        #default three(3) fields as 'username', 'password1' and 'password2'
        fields=[ "username","email","first_name","last_name","contact_number","password1","password2" ]
        
  