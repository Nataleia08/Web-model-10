from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class UsersSite(models.Model):
    username = models.CharField(max_length=200, default="username", )
    email = models.CharField(max_length=200, default="email@example.com")
    password = models.CharField(max_length=200, default="default password")
    first_name = models.CharField(max_length=200, default="default first name")
    last_name = models.CharField(max_length=200, default="default last name")
    phone = models.CharField(max_length=200, default="+380 00 0000000")



    def __str__(self):
        return f"{self.username}"
