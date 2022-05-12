from django import forms
from .models import Post
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):

	class Meta:
		model = Post	
		fields = ('description', 'title', 'featured_image')

		widgets = {
			'description': forms.TextInput(attrs={'class': 'form-control'}),
			'title': forms.TextInput(attrs={'class': 'form-control'}),
		}