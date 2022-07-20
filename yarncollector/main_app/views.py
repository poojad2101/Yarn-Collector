from django.shortcuts import render
from .models import Yarn

# Add the yarn class & list and view function below the imports
# class Yarn:  # Note that parens are optional if not inheriting from another class
#   def __init__(self, color, weight, brand):
#     self.color = color
#     self.weight = weight
#     self.brand = brand


# yarns = [
#   Yarn('White', 'worsted weight', 'Lion brand'),
#   Yarn('Red', 'bulky', 'bernat'),
#   Yarn('Varigated', 'fingering weight', 'Caron')
# ]

from django.http import HttpResponse
from .models import Yarn
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Define the home view
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
  return render(request, 'about.html')

  # Add new view
def yarns_index(request):
  yarns = Yarn.objects.all()
  return render(request, 'yarns/index.html', { 'yarns': yarns })

def yarns_detail(request, yarn_id):
  yarn = Yarn.objects.get(id=yarn_id)
  return render(request, 'yarns/detail.html', { 'yarn': yarn })

class YarnCreate(CreateView):
  model = Yarn
  fields = '__all__'

class YarnUpdate(UpdateView):
  model = Yarn
  fields = ['color', 'weight', 'brand']

class YarnDelete(DeleteView):
  model = Yarn
  success_url = '/yarns/'  