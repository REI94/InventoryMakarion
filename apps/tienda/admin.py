from django.contrib import admin

# Register your models here.
from .models import Producto
from .models import Modelo

admin.site.register(Producto)
admin.site.register(Modelo)