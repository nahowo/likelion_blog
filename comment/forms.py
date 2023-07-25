from django import forms
from .models import comment

class PostComment(forms.ModelForm):
    class Meta:
        model=comment
        fields = [
            'post',
            'author',
            'content',
        ]