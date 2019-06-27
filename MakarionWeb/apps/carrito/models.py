from django.db import models

# Create your models here.
from apps.producto.models import Producto
# Create your models here.

class Carrito(models.Model):

    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null = True)