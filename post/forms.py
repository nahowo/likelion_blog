from django import forms
from .models import post

class PostForm(forms.ModelForm):
    class Meta:
        model=post
        field = (
            'title',
            'author',
            'image',
            'description',
            'price',
        )