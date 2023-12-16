from django.db import models
from account.models import user

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=50, unique=True)
    slug=models.SlugField(max_length=200, unique=True, allow_unicode=True, default="test")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural='Categories'
    
class post(models.Model):
    title=models.CharField(max_length=50)
    author=models.ForeignKey(user, on_delete=models.CASCADE, blank=True, null=True)
    content=models.TextField(null=True)
    image=models.ImageField(upload_to='images/', blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at=models.DateTimeField(auto_now=True, blank=True, null=True)
    category=models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)