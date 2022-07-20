from django.forms import ModelForm
from .models import Production

class ProductionForm(ModelForm):
  class Meta:
    model = Production
    fields = ['date', 'content']