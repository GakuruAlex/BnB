from django.http import HttpResponseRedirect
from django.shortcuts import  render

from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from .forms import CreateUserForm

# Create your views here.
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


def loginPage(request):
    if request.method=="POST":
       username= request.POST.get("username")
       password= request.POST.get("password")
        
       user = authenticate(request,username=username,password=password)
        
       if user is not None:
           login(request,user)
           return HttpResponseRedirect(reverse("hosting:dashboard"))
       else:
           messages.info(request,"Username or password is incorrect")
           
    
    return render(request,"accounts/login.html")


def logoutPage(request):
    logout(request)
    return HttpResponseRedirect("accounts:login")