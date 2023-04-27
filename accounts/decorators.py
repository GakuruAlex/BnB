from django.http import HttpResponse
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse

def unautheticated_user(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("hosting:dashboard"))
        else:
           return view_func(request,*args,**kwargs)
    return wrapper_func