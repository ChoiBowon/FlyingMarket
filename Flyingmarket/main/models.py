from django.db import models
from django.contrib.auth.models import AbstractUser




class Goods(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=200)
    #thumbnail = models.ImageField()

    def __str__(self):
        return self.name
