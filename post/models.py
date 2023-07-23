from django.db import models
from account.models import user

# Create your models here.
class post(models.Model):
    title=models.CharField(max_length=50)
    author=models.ForeignKey(user, on_delete=models.CASCADE, blank=True, null=True)
    content=models.TextField(null=True)
    image=models.ImageField(upload_to='images/', blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at=models.DateTimeField(auto_now=True, blank=True, null=True)