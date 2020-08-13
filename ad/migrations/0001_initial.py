# Generated by Django 3.0.8 on 2020-08-13 13:21

import datetime
from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('region', models.CharField(choices=[('Upper West', 'Upper West'), ('Upper East', 'Upper East'), ('North East', 'North East'), ('Northen', 'Northen'), ('Savannah', 'Savannah'), ('Bono East', 'Bono East'), ('Brong Ahafo', 'Brong Ahafo'), ('Oti', 'Oti'), ('Ahafo', 'Ahafo'), ('Ashanti', 'Ashanti'), ('Volta', 'Volta'), ('Greater Accra', 'Greater Accra'), ('Western North', 'Western North'), ('Western', 'Western'), ('Eastern', 'Eastern'), ('Central', 'Central')], max_length=200, null=True)),
                ('category', models.CharField(choices=[('Mobile Phones', 'Mobile Phones'), ('Mobile Accessories', 'Mobile Phone Accessories'), ('Computer Accessories', 'Computer Accessories'), ('TVs', 'TVs'), ('Cameras & Camcorders', 'Cameras & Camcorders'), ('Audio & MP3', 'Audio & MP3'), ('Other Electronics', 'Other Electronics')], max_length=200, null=True)),
                ('price', models.IntegerField()),
                ('brand', models.CharField(max_length=200, null=True)),
                ('published', models.BooleanField(default=False)),
                ('negotiable', models.BooleanField(default=False)),
                ('main_photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('photo_1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('photo_2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('photo_3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('photo_4', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('date_posted', models.DateField(blank=True, default=datetime.datetime.now)),
                ('seller', models.ForeignKey(default=django.contrib.auth.models.User, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]