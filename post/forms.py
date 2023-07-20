from django import forms
from .models import post

class PostForm(forms.ModelForm):
    class Meta:
        model=post
        fields = [
            'title',
            'author',
            'image',
            'content',
        ]
        widgets = {
            'image':forms.ClearableFileInput(attrs={'required':False}),
        }