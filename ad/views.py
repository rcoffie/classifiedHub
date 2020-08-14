from django.shortcuts import render,redirect,get_object_or_404
from .models import *


# Create your views here.



def ads(request):
  ads = Ads.objects.order_by('-date_posted').filter(published=True)
  context = {'ads':ads,}
  return render(request,'ads/shop.html',context)




def ad(request,ad_id):
  ad = get_object_or_404(Ads,pk=ad_id)
  context = {'ad':ad,}
  return render(request,'ads/ad.html',context)
  