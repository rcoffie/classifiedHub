from django.contrib import admin
from . models import *



#working on Table display in admin panel 
class AdsAdmin(admin.ModelAdmin):
  list_display= ('id','title','location','region','price','negotiable','used','published')
  list_display_links = ('title')
  list_editable = ('id','negotiable','published','used')
  serach_fields = ('title','seller','price','location','region')
  list_par_page = 10



# Register your models here.
admin.site.register(Ads,)