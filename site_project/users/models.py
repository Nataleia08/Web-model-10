from django.db import models

# Create your models here.
class UsersSite(models.Model):
    nickname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    login = models.CharField(max_length=200)


    def __str__(self):
        return f"{self.nickname}"