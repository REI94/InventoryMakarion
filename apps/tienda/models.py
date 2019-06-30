from django.db import models

# Create your models here.
class Producto(models.Model):
    TIPO_PRODUCTO = (
        ('BO', 'Bolso'),
        ('CT', 'Cartera'),
        ('CH', 'Cartuchera'),
        ('MO', 'Morral'),
    )

    tipo_producto = models.CharField(max_length = 2, choices = TIPO_PRODUCTO)
    nombre_producto = models.CharField(max_length = 100, blank = False, null = False)
    descripcion = models.TextField(blank = False, null = False)

class Modelo(models.Model):

    producto = models.ForeignKey(Producto, on_delete = models.CASCADE)
    modelo = models.CharField(max_length = 50, blank = False, null = False)
    cantidad = models.IntegerField(blank = False, null = True)    
