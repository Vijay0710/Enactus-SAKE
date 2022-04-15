from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def product_details(request):
    return render(request,'product_details.html')

def say_hello(request):
    return render(request,'index.html',context={'name':'vijay'})
