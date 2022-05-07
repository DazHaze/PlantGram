from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


from cloudinary.models import CloudinaryField
from cloudinary.forms import CloudinaryFileField   
from cloudinary import CloudinaryImage


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    featured_image = CloudinaryField('image', default='placeholder')
    caption = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)
    slug = models.SlugField(max_length=200, null=True, unique=True)

    def __str__(self):
        return self.caption

    def number_of_likes(self):
        return self.likes.count()

    def date(self):
        return self.created_on.date()

    def get_absolute_url(self):
        return reverse('plants:post_detail', args=[self.slug])



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = CloudinaryField('profile_image', default='placeholder')

    def __str__(self):
        return f'{self.user.username} Profile'

