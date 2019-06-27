from django.db import models


from django.urls import reverse
# Create your models here.

class Producto(models.Model):

	codigo = models.CharField(max_length=10, primary_key=True)
	nombre = models.CharField('Nombre del producto', max_length = 50, blank = False, null = False)
	precio = models.FloatField()
	#tipo = models.CharField(max_length=10)
	descripcion = models.TextField('Descripción', blank = False, null = False)
	cantidad = models.IntegerField()
	"""modelo = models.ForeignKey(Modelo, on_delete=models.SET_NULL, null = True)"""
	#modelo = models.ForeignKey(Modelo, on_delete = models.CASCADE)
	imagen = models.ImageField(upload_to="productos", null = False)
	TIPO = (
		('bolso', 'Bolso'),
		('cartera', 'Cartera'),
		('cartuchera', 'Cartuchera'),
		('portalapto', 'PortaLapto'),
		)
	categoria = models.CharField(max_length=10, choices=TIPO, blank=True, help_text='Categoria del Producto')
    


	def __str__(self):
		return self.codigo

	def get_absolute_url(self):
		return reverse('producto-detail', args=[str(self.codigo)])
		
	
	