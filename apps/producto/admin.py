from django.contrib import admin

# Register your models here.

from .models import Producto

class ProductoAdmin(admin.ModelAdmin):
    search_fields = ['codigo', 'nombre',]
    list_display = ('codigo','nombre', 'categoria',)

admin.site.register (Producto, ProductoAdmin)