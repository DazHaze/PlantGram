# Generated by Django 3.2 on 2022-03-25 18:53

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0003_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='location',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user_photo',
        ),
        migrations.AddField(
            model_name='profile',
            name='image',
            field=cloudinary.models.CloudinaryField(default='default.jpg', max_length=255, verbose_name='profile_image'),
        ),
    ]
