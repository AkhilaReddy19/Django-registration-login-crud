# Create your models here.
from django.db import models
from django import forms
from django.contrib.auth.models import AbstractUser

class Profile(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=50)
    phone = models.BigIntegerField()
    gender = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    password = models.CharField(max_length=20)
    confirm_password = models.CharField(max_length=20)
    tandc = models.CharField(max_length=5)

    def __str__(self):
        return self.first_name + " - " + self.last_name

class City(models.Model):
    city1 = models.CharField(max_length=20)

    def __str__(self):
        return self.city1
