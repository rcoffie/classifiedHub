from django.db import models
from datetime import datetime 
from django.contrib.auth.models import User
from django.http import HttpRequest




# Create your models here.

class Ads(models.Model):
  Category=(
    ('Mobile Phones','Mobile Phones'),
    ('Mobile Accessories','Mobile Phone Accessories'),
    ('Computer Accessories','Computer Accessories'),
    ('TVs','TVs'),
    ('Cameras & Camcorders','Cameras & Camcorders'),
    ('Audio & MP3', 'Audio & MP3'),
    ('Other Electronics','Other Electronics')


  )
  
  Region=(
    ('Upper West','Upper West'),
     ('Upper East','Upper East'),
    ('North East','North East'),
    ('Northen','Northen'),
     ('Savannah','Savannah'),
    ('Bono East','Bono East'),
    ('Brong Ahafo','Brong Ahafo'),
    ('Oti','Oti'),
    ('Ahafo','Ahafo'),
    ('Ashanti','Ashanti'),
    ('Volta','Volta'),
    ('Greater Accra','Greater Accra'),
    ('Western North','Western North'),
    ('Western','Western'),
    ('Eastern','Eastern'),
    ('Central','Central'),
  )

  title = models.CharField(max_length=100)
  seller  = models.ForeignKey(User, on_delete=models.DO_NOTHING,default=User)
  city = models.CharField(max_length=50)
  region = models.CharField(max_length=200, null=True,choices=Region)
  category = models.CharField(max_length=200, null=True,choices=Category)
  price = models.IntegerField()
  brand = models.CharField(max_length=200,null=True)
  published = models.BooleanField(default=False)
  negotiable = models.BooleanField(default=False)
  main_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
  photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
  photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
  photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
  photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
  date_posted = models.DateField(default=datetime.now,blank=True)


  def __str__(self):
    return self.title