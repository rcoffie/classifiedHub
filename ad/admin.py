from django.contrib import admin
from . models import *



#working on Table display in admin panel 
class AdsAdmin(admin.ModelAdmin):
  list_display = ('id','title','seller','location','region','price','published','negotiable','date_posted','published','used')
  list_display_links = ('title','seller')
  list_filter = ('title','seller','price','location','region',)
  list_editable = ('id','negotiable','published','used')
  search_fields = ('title','seller','price','location','region')
  list_per_page  = 10



# Register your models here.
admin.site.register(Ads,AdsAdmin)