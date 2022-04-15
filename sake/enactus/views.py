from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def login(request):
    return render(request,'login.html')


def admin_01(request):
    context = {
        "data" : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    }
    # return response
    return render(request, "admin_01.html", context)
    
def admin_02(request):
    context = {
        "data" : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    }
    # return response
    return render(request, "admin_02.html", context)

def profile_01(request):
    context = {
        "data" : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    }
    # return response
    return render(request, "profile_01.html", context)

def register(request):
    return render(request,'register.html')

def product_details(request):
    return render(request,'product_details.html')

def say_hello(request):
    return render(request,'index.html',context={'name':'vijay'})
