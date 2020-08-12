from django.shortcuts import render,redirect

# Create your views here.



def ads(request):
  return render(request,'ads/ads.html')