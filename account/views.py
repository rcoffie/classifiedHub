from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.contrib.auth import logout


# Create your views here.

def login(request):
  return render(request,'account/login.html')



def register(request):
  return render(request,'account/registration.html')