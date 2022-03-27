from django import forms
from .models import Post
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('caption', 'slug', 'featured_image')

		widgets = {
			'caption': forms.TextInput(attrs={'class': 'form-control'}),
			'slug': forms.TextInput(attrs={'class': 'form-control'}),
		}