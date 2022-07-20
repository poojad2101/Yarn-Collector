from django.contrib import admin
# import your models here
from .models import Yarn, Production

# Register your models here
admin.site.register(Yarn)
admin.site.register(Production)



