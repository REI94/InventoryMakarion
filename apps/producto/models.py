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
	precio = models.DecimalField(max_digits=18, decimal_places=2)
	precio_en_descuento = models.DecimalField(max_digits=18, decimal_places=2, blank = True, null = True)
	descripcion = models.TextField('Descripción', blank = False, null = False)
	cantidad = models.IntegerField()
	disponible = models.BooleanField(default=True)
	creado_el = models.DateTimeField(auto_now_add=True)
	actualizado_el = models.DateTimeField(auto_now=True)
	imagen = models.ImageField('Imágen principal', upload_to="productos", null = True, blank = True)
	imagen_2 = models.ImageField('Imágen 2', upload_to="productos", null = True, blank = True)
	imagen_3 = models.ImageField('Imágen 3', upload_to="productos", null = True, blank = True)
	imagen_4 = models.ImageField('Imágen 4', upload_to="productos", null = True, blank = True)
	imagen_5 = models.ImageField('Imágen 5', upload_to="productos", null = True, blank = True)
	texto_destacado = models.CharField('Texto destacado', max_length=100, blank = True)
	caracteristica_destacada = models.CharField('Característica destacada 1', max_length=60, blank=True, null=True)
	caracteristica_destacada_2 = models.CharField('Característica destacada 2', max_length=60, blank=True, null=True)
	caracteristica_destacada_3 = models.CharField('Característica destacada 3', max_length=60, blank=True, null=True)
	caracteristica_destacada_4 = models.CharField('Característica destacada 4', max_length=60, blank=True, null=True)
	caracteristica_destacada_5 = models.CharField('Característica destacada 5', max_length=60, blank=True, null=True)

	def __str__(self):
		cadena = str(self.codigo)+" - "+self.nombre
		return cadena

	def get_absolute_url(self):
		return reverse('producto-detail', args=[str(self.codigo)])		