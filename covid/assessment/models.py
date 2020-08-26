from django.db import models

# Create your models here.
class UserData(models.Model):
    name = models.CharField(max_length=255)
    age = models.CharField(max_length=255)
    sex = models.CharField(max_length=255)
    temp = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    score = models.CharField(max_length=255)
    result = models.CharField(max_length=255)