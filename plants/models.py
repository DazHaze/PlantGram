from django.db import models
from django.utils import timezone
from cloudinary.models import CloudinaryField


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    featured_image = CloudinaryField('image', default='placeholder')
    caption = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)