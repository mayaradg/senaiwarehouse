from django.db import models
from feedstock.models import Feedstock
# Create your models here.

class Address(models.Model):
    area = models.CharField(max_length=10)
    street = models.CharField(max_length=10)
    module = models.CharField(max_length=10)
    level = models.CharField(max_length=10)
    box = models.CharField(max_length=10, null=True, blank=True)
    feedstock = models.OneToOneField(Feedstock, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.area + self.street + self.module + self.level

