from django.contrib import admin

# Register your models here.

from .models import Producto

class ProductoAdmin(admin.ModelAdmin):
    search_fields = ['codigo', 'tipo',]
    list_display = ('codigo','tipo', 'categoria',)

admin.site.register (Producto, ProductoAdmin)