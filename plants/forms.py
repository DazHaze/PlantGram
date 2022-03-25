from django import forms
from cloudinary.forms import CloudinaryFileField
from .models import Profile


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image',)
        image = CloudinaryFileField(
            options={
                'tags': "directly_uploaded",
                'crop': 'limit', 'width': 1000, 'height': 1000,
                'eager': [{'crop': 'fill', 'width': 150, 'height': 100}]
            })
