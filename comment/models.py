from django.db import models
from post.models import post
from account.models import user

# Create your models here.
class comment(models.Model):
    post=models.ForeignKey(post, on_delete=models.CASCADE, null=True)
    author=models.ForeignKey(user, on_delete=models.CASCADE, null=True)
    content=models.TextField(null=True)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)