from django.db import models
from django.urls import reverse

# Create your models here.
class Yarn(models.Model):
    color = models.CharField(max_length=100)
    weight = models.CharField(max_length=100)
    brand = models.TextField(max_length=250)
    
    
    def __str__(self):
      return self.color

    def get_absolute_url(self):
      return reverse('detail', kwargs={'yarn_id': self.id})

class Production(models.Model):
    date = models.DateField('production date')
    content = models.CharField(
      max_length=100)
#       # add the 'choices' field option
#     choices=
#     # set the default value for meal to be 'B'
#     default=MEALS[0][0]
#   )
    yarn = models.ForeignKey(Yarn, on_delete=models.CASCADE)

    def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
     return f"{self.content()} on {self.date}"
