# Generated by Django 3.0.8 on 2020-08-13 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0003_ads_used'),
    ]

    operations = [
        migrations.AddField(
            model_name='ads',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
