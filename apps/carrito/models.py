from django.db import models

from apps.producto.models import Producto
# Create your models here.

class Carrito(models.Model):

    idCarrito = models.AutoField(primary_key=True)
    producto = models.ManyToManyField(Producto)
    total = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)
    cantidadAgregada = models.IntegerField()

    def __str__(self):
        return str(self.idCarrito)