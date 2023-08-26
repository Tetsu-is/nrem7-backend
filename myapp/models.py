from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=1000)
    price = models.IntegerField(default=0)

class General(models.Model):
    deadline = models.DateField()
    requiredtime = models.DurationField()