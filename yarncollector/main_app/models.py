from django.db import models

# Create your models here.
class Yarn(models.Model):
    color = models.CharField(max_length=100)
    weight = models.CharField(max_length=100)
    brand = models.TextField(max_length=250)
    
