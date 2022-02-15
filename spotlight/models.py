from django.db import models
from django.forms import EmailField

# Create your models here.
class Profile(models.Model):
    bio = models.TextField(max_length=500, default="My Bio", blank=True)
    projects = models.CharField(blank=True, max_length=120)
    email = models.EmailField(max_length=100)
    

    def __str__(self):
        return self.bio


class Project(models.Model):
    title = models.CharField(max_length=250, blank=True)
    description = models.TextField(max_length=250, blank=True)
    links= models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.title