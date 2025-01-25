from django.db import models

class Question(models.Model):
    qno=models.IntegerField(primary_key=True,auto_created=True)
    que=models.CharField(max_length=200)
    optiona=models.CharField(max_length=100)
    optionb=models.CharField(max_length=100)
    optionc=models.CharField(max_length=100)
    optiond=models.CharField(max_length=100)
    answer=models.CharField(max_length=1) 

class User(models.Model):
    username=models.CharField(primary_key=True,max_length=50)
    password=models.CharField(max_length=20)
    fullname=models.CharField(max_length=100)

