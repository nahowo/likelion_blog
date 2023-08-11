from django import forms
from .models import post, Category

class PostForm(forms.ModelForm):
    category=forms.ModelChoiceField(queryset=Category.objects.all(),widget=forms.Select)
    class Meta:
        model=post
        fields = [
            'title',
            'image',
            'content',
            'category',
        ]
        widgets = {
            'image':forms.ClearableFileInput(attrs={'required':False}),
        }