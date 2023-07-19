from django.db import models

# Create your models here.
class Login(models.Model):
    email=models.CharField(max_length=50)
    repeatpassword=models.CharField(max_length=50)
    invitecode=models.CharField(max_length=50)
class Registermodel(models.Model):
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    repeatpassword=models.CharField(max_length=50)