from django.db import models

# Create your models here.


class reg(models.Model):
    name=models.CharField(max_length=40)
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=15)
    contact=models.CharField(max_length=40)