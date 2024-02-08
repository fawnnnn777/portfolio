from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser

class User(AbstractUser):
    pass

class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    description = models.TextField()
    phone = models.TextField()
    email = models.TextField()
    project = models.CharField(max_length=50)
    project_description = models.TextField()
    link = models.TextField()
    style = models.TextField()

    
# Create your models here.
