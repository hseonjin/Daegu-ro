from django.db import models

# Create your models here.
class Map(models.Model):
    name = models.CharField(max_length=50)
    lat = models.DecimalField(max_digits=11, decimal_places=5)
    lon = models.DecimalField(max_digits=11, decimal_places=5)
    def __str__(self):
        return self.name