from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class Authors(models.Model):

    fullname = models.CharField(max_length=200, unique=True)
    born_date = models.DateField()
    born_location = models.CharField(max_length=200)
    description = models.CharField(max_length=20000)
    # created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.fullname}"

class Tag(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)

    def __str__(self):
        return f"{self.name}"


class Quotes(models.Model):
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(Authors, on_delete=models.CASCADE)
    quote = models.CharField(max_length=20000)
    # created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quote}, {self.author}. Tags: {self.tags}"





