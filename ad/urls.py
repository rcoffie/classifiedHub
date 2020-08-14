from django.urls import path
from . import views 

urlpatterns = [
   path('',views.ads,name='ads'),
   path('<int:ad_id>',views.ad,name='ad'),
]
