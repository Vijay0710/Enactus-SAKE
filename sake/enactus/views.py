from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def login(request):
    return render(request,'login.html')

def say_hello(request):
    return render(request,'index.html',context={'name':'vijay'})
