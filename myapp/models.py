from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=1000)
    price = models.IntegerField(default=0)

class General(models.Model):
    deadline = models.DateField()
    requiredtime = models.DurationField()

class Time(models.Model):
    acountName = models.CharField(max_length=1000)
    acountNumber = models.IntegerField(default=0, unique=True)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    key = models.IntegerField(unique=True)
    