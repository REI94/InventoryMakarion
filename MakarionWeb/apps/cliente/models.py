from django.db import models

# Create your models here.
class Persona(models.Model):

	cedula = models.CharField(max_length=10, primary_key=True)	
	nombre = models.CharField(max_length=50)
	apellidos = models.CharField(max_length=70)
	edad = models.IntegerField()
	direccion = models.TextField()
	telefono = models.CharField(max_length=12)
	email = models.EmailField()
	
	class Meta:
		abstract = True


class Cliente(Persona):
	rif = models.CharField(max_length=12, null = True, blank = True)
	
	def __str__(self):
		return self.cedula