from django.contrib import admin

# Register your models here.

from .models import Producto

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nombre', 'precio', 'precio_en_descuento', 'cantidad', 'disponible', 'creado_el', 'actualizado_el']
    list_filter = ['disponible', 'creado_el', 'actualizado_el']
    list_editable = ['precio', 'precio_en_descuento', 'cantidad', 'disponible']

admin.site.register (Producto, ProductoAdmin)