from django.db import models
from annoying.fields import AutoOneToOneField

# Create your models here.
class Cliente(models.Model):
    TIPO_DOCUMENTO_ID = (
        ('V', 'Venezolano'),
        ('E', 'Extranjero'),
        ('P', 'P - RIF'),
        ('J', 'J- RIF'),
        ('G', 'G - RIF'),
        ('R', 'R - Firma personal'),
    )

    nombre = models.CharField('Nombre', max_length = 50, blank = False, null = False)
    apellido = models.CharField('Apellido', max_length = 50, blank = False, null = False)
    tipo_documento_id = models.CharField('Tipo documento de identidad', max_length = 1, blank = False, null = False, choices = TIPO_DOCUMENTO_ID)
    num_documento_id = models.CharField('Número documento de identidad', max_length = 12, blank = False, null = False)
    edad = models.IntegerField('Edad', blank = False, null = False)
    telefono = models.CharField('Teléfono', max_length = 15, blank = False, null = False)
    direccion = models.CharField('Dirección', max_length = 50, blank = False, null = False)
    email = models.CharField('Correo electrónico', max_length = 50, blank = False, null = False)
    contrasenia = models.CharField('Contraseña', max_length = 60, blank = False, null = False)

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

    #cliente_asociado = models.OneToOneField(Cliente, on_delete = models.CASCADE)
    cliente_asociado = AutoOneToOneField(Cliente, on_delete = models.CASCADE, primary_key=True)
    cant_productos = models.IntegerField('Productos en el carrito', blank = False, null = False, default = 0)
    producto_en_carrito = models.ManyToManyField(Producto, blank = True)