from django.db import models

# Create your models here.

from apps.cliente.models import Persona

# Create your models here.

class Administrador(Persona):
	sueldo = models.FloatField()
	
	def __str__(self):
		return self.cedula