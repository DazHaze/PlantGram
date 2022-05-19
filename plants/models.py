from django.db import models, IntegrityError
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
import random


from cloudinary.models import CloudinaryField
from cloudinary.forms import CloudinaryFileField   
from cloudinary import CloudinaryImage


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    featured_image = CloudinaryField('image', default='placeholder')
    description = models.TextField()
    title = models.TextField(default="placeholder")
    created_on = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)
    slug = models.SlugField(max_length=200, null=True, unique=True)

    def save(self, *args, **kwargs):
        try:
            self.slug = ''.join(str(random.randint(0, 9)) for _ in range(8))
            super().save(*args, **kwargs)
        except IntegrityError:
            self.save(*args, **kwargs)

    def number_of_likes(self):
        return self.likes.count()

    def date(self):
        return self.created_on.date()

    def get_absolute_url(self):
        return reverse('plants:post_detail', args=[self.slug])

    def __str__(self):
        return f'{self.title}'



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = CloudinaryField('profile_image', default='placeholder')

    def __str__(self):
        return f'{self.user.username} Profile'

class Picture(models.Model):
    image = CloudinaryField('image')

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.__str__(), self.name)

