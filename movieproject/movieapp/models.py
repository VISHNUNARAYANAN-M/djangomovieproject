from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Movies(models.Model):
    name = models.CharField(max_length=250, unique=True)
    img = models.ImageField(upload_to='movieimage', blank=True)
    description = models.TextField(blank=True)
    releasedate = models.DateField(auto_now=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    actors = models.TextField(blank=True)
    trailerlink=models.TextField(blank=True)


    def __str__(self):
        return self.name