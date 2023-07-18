from django.db import models

# Create your models here.
class post(models.Model):
    title=models.CharField(max_length=50)
    author=models.CharField(max_length=20)
    content=models.TextField(null=True)
    image=models.ImageField(null=True)
    date=models.DateTimeField()