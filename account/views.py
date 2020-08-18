from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.contrib.auth import logout


# Create your views here.

def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username,password=password)
    if user is not None:
      auth.login(request,user)
      messages.success(request,'login successfully')
      return redirect('dashboard')
    else:
      messages.error(request,'password or username error')
      return redirect('login')

  return render(request,'account/login.html')



def register(request):
  if request.method == 'POST':
    first_name = request.POST['first_name']
    last_name  = request.POST['last_name']
    username   = request.POST['username']
    email      = request.POST['email']
    password   = request.POST['password']
    password2  = request.POST['password2']
    if password == password2:
      if User.objects.filter(username=username).exists():
        messages.error(request,'username alerady exits')
        return redirect('register')
      else:
        if User.objects.filter(email=email).exists():
          messages.error(request,'email address already taken')
          return redirect ('register')
        else:
          user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password) 
          user.save() 
          messages.success(request,'account created successfully you can now login ') 
          return redirect('login')
    else:
      messages.error(request,'password dont match')
      return redirect('register')

      

  return render(request,'account/registration.html')



def dashboard(request):
    return render(request,'account/dashboard.html')