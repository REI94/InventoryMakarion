from django.db import models

# Create your models here.
class Compra(models.Model):
	
	idCompra = models.AutoField(primary_key=True)
	fecha = models.DateTimeField(auto_now_add=True)
	MontoTotal = models.DecimalField(max_digits=18, decimal_places=2)

	def __str__(self):
		return str(self.idCompra)
	