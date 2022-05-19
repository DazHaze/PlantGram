from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):

	class Meta:
		model = Post	
		fields = ('description', 'title', 'featured_image')

		widgets = {
			'description': forms.TextInput(attrs={'class': 'form-control'}),
			'title': forms.TextInput(attrs={'class': 'form-control'}),
		}

class CommentForm(forms.ModelForm):

	class Meta:
		model = Comment
		fields = ('body',)
