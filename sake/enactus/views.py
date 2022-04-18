from logging import error
from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.contrib import messages
from enactus.forms import RegisterForm
import pyrebase
import traceback
import re
import json
# Create your views here.

firebaseConfig = {
    "apiKey": "AIzaSyCyhztJuQz4QNgR3cYkNCAKodHKNT3maC4",
    "authDomain": "enactus-sake.firebaseapp.com",
    "databaseURL": "https://enactus-sake-default-rtdb.firebaseio.com",
    "projectId": "enactus-sake",
    "storageBucket": "enactus-sake.appspot.com",
    "messagingSenderId": "920466632092",
    "appId": "1:920466632092:web:2e73db896459892ccaec59",
    "measurementId": "G-6E2KRGTTPV"
}
firebase = pyrebase.initialize_app(firebaseConfig)
def thankyou(request):
    return render(request,'thankyou.html')

def profile_02(request):
    return render(request,'profile_02.html')

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
    if request.method == 'POST':
        FailedMessages = {'FailureMessage1': 'Username is invalid',
                           'FailureMessage2':'Email is invalid',
                           'FailureMessage3':'Password doesn\'t Follow Pattern'    
                          }
        no = []
        errorMessage = []
        uname=umail=Pass=cpass=''
        print("Testing "+FailedMessages['FailureMessage1'])
        print('Yes')
        uname = request.POST.get('uname',None)
        umail = request.POST.get('umail',None)
        cpass = request.POST.get('cpass',None)
        Pass = request.POST.get('Pass',None)
        print(uname,umail,Pass,cpass)
        emailRegex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        passwordReg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$"
        match_passwordregex = re.compile(passwordReg)
        if(Pass != cpass or not re.search(match_passwordregex,Pass)):
            errorMessage.append(FailedMessages['FailureMessage3'])
        if(umail=='' or not re.fullmatch(emailRegex,umail)):
            errorMessage.append(FailedMessages['FailureMessage2'])
        if(uname == "" or  len(uname)<4):
            errorMessage.append(FailedMessages['FailureMessage1'])   
        print(errorMessage)
        if(not errorMessage):
            try:
                auth = firebase.auth()
                auth.create_user_with_email_and_password(umail, Pass)
                print('Created user ', umail)
                return render(request,'register.html')
            except Exception as e:
                exc = str(e).strip()
                i_pose = exc.index(']')
                exc = exc[i_pose+1:]
                print(type(exc))
                print(exc)
                json_obj = json.loads(exc)
                val = json_obj['error']['errors']
                errorMessage.append(val[0]['message'])
                context = {'messages':errorMessage}
                return render(request,'register.html',context)
        else:
            context = {'messages':errorMessage}
            print(len(context['messages']))
            return render(request,'register.html',context)
    return render(request,'register.html')

def product_details(request):
    return render(request,'product_details.html')

def say_hello(request):
    return render(request,'index.html',context={'name':'vijay'})
