from django.http import HttpResponseRedirect
from django.shortcuts import  render

from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from .forms import CreateUserForm
from .decorators import unautheticated_user

# Create your views here.
@unautheticated_user
def signup(request):
    form = CreateUserForm()
    if request.method == 'POST':
     form = CreateUserForm(request.POST)
     if form.is_valid():
         form.save()
         user =form.cleaned_data.get("username")
         messages.success(request,"Account successfully created for "+ user)
         
         return HttpResponseRedirect(reverse("accounts:login"))
    return render(request,"accounts/signup.html",{"form":form})

@unautheticated_user
def loginPage(request):
    if request.method=="POST":
       username= request.POST.get("username")
       password= request.POST.get("password")
        
       user = authenticate(request,username=username,password=password)
        
       if user is not None:
           login(request,user)
           messages.success(request,"Welcome "+ username)
           return HttpResponseRedirect(reverse("hosting:dashboard"))
       else:
           messages.info(request,"Username or password is incorrect")
           
    
    return render(request,"accounts/login.html")


def logoutPage(request):
    logout(request)
    return HttpResponseRedirect(reverse("accounts:login"))