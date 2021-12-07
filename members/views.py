from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
 
# Create your views here.
 
'''def register(response):
    if response.method=="POST":
        #check this
        userForm=RegisterForm(response.POST)
        if userForm.is_valid():
            userForm.save()
        return redirect("/home")    
    else:    
        userForm=UserCreationForm()
        
    return render(response,"authentication/register.html",{"userForm":userForm})

'''


