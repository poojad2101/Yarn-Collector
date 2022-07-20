from django.db import models
from django.urls import reverse

# Create your models here.
class Yarn(models.Model):
    color = models.CharField(max_length=100)
    weight = models.CharField(max_length=100)
    brand = models.TextField(max_length=250)
    
    
    def __str__(self):
       return self.name

    def get_absolute_url(self):
       return reverse('detail', kwargs={'yarn_id': self.id})

