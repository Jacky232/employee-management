from django.db import models

# Create your models here.

class Employee(models.Model):
    idnum=models.CharField(max_length=100,null=True, blank=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=150)
    phone=models.CharField(max_length=50)
    address=models.CharField(max_length=200)