from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import user

class SignupForm(UserCreationForm):
    class Meta:
        model = user
        fields = ['username','password1','password2','nickname','email']

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = user
        fields = ['username','nickname','email']