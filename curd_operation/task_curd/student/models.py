from django.db import models



class reg(models.Model):
    name=models.CharField(max_length=40)
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=15)
    contact=models.CharField(max_length=40)
    address=models.CharField(max_length=100,default='Pune')
    
    
# class student(models.Model):
#     name=models.CharField(max_length=40)
#     email=models.CharField(max_length=30)
#     password=models.CharField(max_length=15)
#     contact=models.CharField(max_length=40)
#     address=models.CharField(max_length=100)