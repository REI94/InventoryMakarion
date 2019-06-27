from django.db import models

# Create your models here.
from apps.producto.models import Producto
from apps.cliente.models import Cliente


# Create your models here.
class Compra(models.Model):
	idCompra = models.CharField(max_length=10, primary_key=True)
	producto = models.ManyToManyField(Producto)
	fecha = models.DateField()
	cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null = True)

	def __str__(self):
		return self.idCompra  
	
	
	"""
	producto = models.ForeignKey(Producto)
	(auto_now_add=True)
	"""