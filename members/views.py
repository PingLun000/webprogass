 
 
from django.contrib.auth.models import Group, User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout as logOut
from django.http import request
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .registrationform import registerationForm

 
# Create your views here.

'''def login(request):
    if request.method=='POST':
        membersForm=registerationForm(data=request.POST)
        if membersForm.is_valid():
            member=membersForm.get_user()
            logins(request,member)
        return redirect("/home")    
    else:
        membersForm=registerationForm()
            
    return render(request,"registration/login.html",{'membersForm':membersForm})


'''

'''def signIn(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')

        signInRequest=AuthenticationForm(data=request.POST)
        if signInRequest.is_valid():
            return redirect('store:storeProducts')
    else:
        signInRequest=AuthenticationForm()
        return redirect('members:signIn')
    context={}
    return render(request,'authentication/signIn.html',context)     
    
    '''
    
'''def signIn(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')

        try:
            user=User.object.get(email=email,password=password)
        except:
            # used to show error message while email!=email https://docs.djangoproject.com/en/3.2/ref/contrib/messages/
            messages.error(request, 'Member doesn\'t exsit ')
        #return user object
        user=authenticate(request,email=email,password=password)

        if user is not None:
            login(request,user)
            return redirect('store:storeProducts')
           # messages.success(request, 'Sign In Successful ')
        else :
            messages.error(request, 'Member email/pass doesn\'t exsit ')
            return redirect('members:signIn')
    context={}
    return render(request,'authentication/signIn.html',context)'''
    
def register(request):
    if request.method=='POST':
        #check this
        membersForm=registerationForm(request.POST)
        if membersForm.is_valid():
            member=membersForm.save()
            username=membersForm.cleaned_data.get('username')
            signup_user=User.objects.get(username=username)
            membersGroup=Group.objects.get(name='membersGroup')
            membersGroup.user_set.add(signup_user)
            login(request,member) 

        return redirect('store:storeProducts')    
    else:
        membersForm=registerationForm()
            
    return render(request,"registration/register.html",{'membersForm':membersForm})
 


def logout(request):
    if request.method=='POST':
        logOut(request)
        return redirect('/login')
