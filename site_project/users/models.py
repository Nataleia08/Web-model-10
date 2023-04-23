from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class UsersSite(models.Model):
    nickname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    login = models.CharField(max_length=200)
    avatar = models.ImageField(default='default_avatar.png', upload_to='profile_images')


    def __str__(self):
        return f"{self.nickname}"

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 250 or img.width > 250:
            new_img = (250, 250)
            img.thumbnail(new_img)
            img.save(self.avatar.path)