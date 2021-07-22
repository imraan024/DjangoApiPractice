from django.db import models
from django.db.models.expressions import F

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100, null= False, blank = False)
    price = models.DecimalField(max_digits= 6, decimal_places=2)
    category = models.CharField(max_length=100, null=False, blank= False)
    description = models.TextField()

    def __str__(self):
        return self.name
