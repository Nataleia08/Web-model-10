from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class Authors(models.Model):

    fullname = models.CharField(max_length=200)
    born_date = models.DateField()
    born_location = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)

    def __str__(self):
        return f"{self.fullname}"



class Quotes(models.Model):
    tags = ArrayField(models.CharField(max_length=30), size=10)
    author = models.ForeignKey(Authors, on_delete=models.CASCADE)
    quote = models.CharField(max_length=2000)

    def __str__(self):
        return f"{self.quote}, {self.author}. Tags: {self.tags}"





