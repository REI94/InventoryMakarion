from django.db import models

# Create your models here.
		
class Producto(models.Model):
	"""
	TIPO = (
        ('c', 'Cartuchera'),
        ('b', 'Bolso'),
        ('cartera', 'Cartera'),
        ('pCos', 'Porta Cosmetico'),
        ('pL', 'Porta Lapto'),
        ('pCanaima', 'Porta Canaima'),
        ('pT', 'Porta Tablet'),
        ('b', 'Porta Canaima'),
        
    )
	"""
	

	codigo = models.CharField(max_length=10, primary_key=True)
	precio = models.FloatField()
	tipo = models.CharField(max_length=10)
	cantidad = models.IntegerField()
	"""modelo = models.ForeignKey(Modelo, on_delete=models.SET_NULL, null = True)"""
	#modelo = models.ForeignKey(Modelo, on_delete = models.CASCADE)
	imagen = models.ImageField(upload_to="productos", null = False)
	TIPOO = (
		('bolso', 'Bolso'),
		('cartera', 'Cartera'),
		('cartuchera', 'Cartuchera'),
		('portalapto', 'PortaLapto'),
		)
	categoria = models.CharField(max_length=10, choices=TIPOO, blank=True, help_text='Categoria del Producto')
    


	def __str__(self):
		return self.codigo

	
	