import telnetlib
from unicodedata import name
from django.db import models

# Create your models here.
class Info(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    tel = models.CharField(max_length=50)
    contents = models.CharField(max_length=5000)

    def __str__(self):
        return self.name