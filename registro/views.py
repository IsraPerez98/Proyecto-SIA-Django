from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegistroForm

from django.http import HttpResponse
# Create your views here.

#def index(response):
#    return HttpResponse("<h1>registro</h1>")

def registro(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        
        #return redirect("/")
    else:
        form = RegisterForm()

    return render(response, "registro/registro.html", {"form":form})

def login(request,*args,**kwargs):
    pass