from django.shortcuts import render

# Add the yarn class & list and view function below the imports
class Yarn:  # Note that parens are optional if not inheriting from another class
  def __init__(self, color, weight, brand, ):
    self.color = color
    self.weight = weight
    self.brand = brand


yarns = [
  Yarn('White', 'worsted weight', 'Lion brand'),
  Yarn('Red', 'bulky', 'bernat'),
  Yarn('Varigated', 'fingering weight', 'Caron')
]

from django.http import HttpResponse

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
  return render(request, 'about.html')

  # Add new view
def yarns_index(request):
  return render(request, 'yarns/index.html', { 'yarns': yarns })