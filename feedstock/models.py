from django.db import models
# Create your models here.

class Feedstock(models.Model):
    name = models.CharField(max_length=25)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name
