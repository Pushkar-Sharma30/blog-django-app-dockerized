from django.db import models
from django.contrib.auth.models import User
# from django_resized import ResizedImageField

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.name
    


class Blog(models.Model):
    title = models.TextField(max_length=200)
    authors = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    content = models.TextField(max_length=10000, blank=False, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField (upload_to='uploaded', null=True)
    created_at = models.DateField(auto_now=True, null=True)
    updated_at = models.DateField(auto_now=True, null=True)

    def __str__(self):
        return self.title
    

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    message = models.TextField(max_length=5000, blank=False, null=True)

    def __str__(self):
        return self.email