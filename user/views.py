from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.shortcuts import get_object_or_404, render,redirect
import urllib
import http.client
import json
import requests
import responses
from .models import travel,Items

# Create your views here.
def signup(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']

        if password1==password2:    
                if User.objects.filter(email=email).exists(): 
                    messages.info(request,'User already exists')
                    return redirect('/')
                else:
                    user=User.objects.create_user(username=email,first_name=first_name,last_name=last_name,password=password1,email=email)
                    user.save()
                    
                    # requests.post('https://api.kaleyra.io/v1/HXIN1709604395IN/voice/outbound?to=+919999196461&api-key=A7d9a93081fcd9840089b138b995e51c4&bridge=+918046983237&target=[{"message":{"text":"enter"} }])
                    url = "https://api-voice.kaleyra.com/v1/?method=voice.json&api_key=A2943763b1bdad7660XXXXXXXXXX80e3a&format=json"

                    payload = json.dumps({
                    "play": "123.sound",
                    "call": [
                        {
                        "to": "+919483096270",
                        "play": "123.sound",
                        "meta": {
                            "param1 ": "value1",
                            "param2 ": "value2"
                        }
                        },
                    ]
                    })
                    headers = {
                    'Content-Type': 'application/x-www-form-urlencoded'
                    }

                    response = requests.request("POST", url, headers=headers, data=payload)

                    print(response.text)
 
                return redirect('login/')

    else:
        return render(request,"user/signup.html")

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        try:
            usr=User.objects.get(username=username)
        except:
            messages.info(request,'User doesnot exist please register')
            return redirect('/login')    


        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return HttpResponse("user succesfully logged in")

        else:
            messages.info(request,'Invalid Credentials')
            return redirect('user:home')    

    else:
        
        return render(request,'user/login.html')

def home(request):
    travl=travel.objects.filter(user=request.user)
    items=Items.objects.filter(travel=travl)
    context={
        'travel':travl,
        'items':items
    }
    return render(request,"user/home.html",context)

def create_travel(request):
    if request.method=='POST':
        travelname=request.POST['travelname']
        returndate=request.POST['returndate']
        durationoftravel=request.POST['durationoftravel']
        travl=travel.objects.create(user=request.user,travelname=travelname,returndate=returndate,durationoftravel=durationoftravel)
        travl.save()
        return redirect('user:home')
    else:
        return render(request,"user/createtravel.html")    



 