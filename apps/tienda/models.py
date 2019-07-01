from django.db import models

# Create your models here.
class Producto(models.Model):
    TIPO_PRODUCTO = (
        ('BO', 'Bolso'),
        ('CT', 'Cartera'),
        ('CH', 'Cartuchera'),
        ('MO', 'Morral'),
    )

    tipo_producto = models.CharField('Tipo de producto', max_length = 2, choices = TIPO_PRODUCTO)
    nombre_producto = models.CharField('Nombre del producto', max_length = 100, blank = False, null = False)
    descripcion = models.TextField('Descripción', blank = False, null = False)

    def __str__(self):
        return self.nombre_producto

class Modelo(models.Model):

    producto = models.ForeignKey(Producto, on_delete = models.CASCADE)
    modelo = models.CharField(max_length = 50, blank = False, null = False)
    cantidad = models.IntegerField(blank = False, null = True)    

    def __str__(self):
        return self.modelo        

class Carrito(models.Model):

    cant_productos = models.IntegerField('Productos en el carrito', blank = True, null = True)
    producto_en_carrito = models.ManyToManyField(Producto, blank = True)