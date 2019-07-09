from django.db import models


from django.urls import reverse
# Create your models here.

class Producto(models.Model):
	TIPO = (
		('bolso', 'Bolso'),
		('cartera', 'Cartera'),
		('cartuchera', 'Cartuchera'),
		('portalapto', 'PortaLapto'),
		)

	codigo = models.CharField(max_length=10, primary_key=True)
	nombre = models.CharField('Nombre del producto', max_length = 50, blank = False, null = False)
	categoria = models.CharField(max_length=10, choices=TIPO, blank=True, help_text='Categoria del Producto')
	precio = models.FloatField()
	precio_en_descuento = models.FloatField(blank = True, null = True)
	descripcion = models.TextField('Descripción', blank = False, null = False)
	cantidad = models.IntegerField()
	disponible = models.BooleanField(default=True)
	unidades_vendidas = models.PositiveIntegerField(default=0)
	creado_el = models.DateTimeField(auto_now_add=True)
	actualizado_el = models.DateTimeField(auto_now=True)
	imagen = models.ImageField(upload_to="productos", null = False)
	texto_destacado = models.CharField('Texto destacado', max_length=100, blank = True)
	caracteristica_destacada = models.CharField('Característica destacada', max_length=60, blank=True)

	def __str__(self):
		cadena = str(self.codigo)+" - "+self.nombre
		return cadena

	def get_absolute_url(self):
		return reverse('producto-detail', args=[str(self.codigo)])