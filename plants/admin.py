from django.contrib import admin
from .models import Post
from .models import Profile
from .models import Picture, Comment

# Register your models here.
admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Picture)
admin.site.register(Comment)