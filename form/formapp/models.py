from django.db import models

# Create your models here.
class Register(models.Model):
    Name=models.CharField(max_length=50)
    Place=models.CharField(max_length=50)
    Age=models.CharField(max_length=50)
    Email=models.CharField(max_length=50)
class Login(models.Model):
    username=models.CharField(max_length=50)    
    password=models.CharField(max_length=50)
    type=models.CharField(max_length=50)