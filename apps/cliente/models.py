from django.db import models

# Create your models here.
class Persona(models.Model):
	TIPO_DOCUMENTO_ID = (
        ('V', 'Venezolano'),
        ('E', 'Extranjero'),
        ('P', 'P - RIF'),
        ('J', 'J- RIF'),
        ('G', 'G - RIF'),
        ('R', 'R - Firma personal'),
    )
	
	tipo_documento_id = models.CharField('Tipo documento de identidad', max_length = 1, blank = False, null = False, choices = TIPO_DOCUMENTO_ID)
	documento_id = models.CharField('Documento de identidad', primary_key = True, max_length = 12, blank = False, null = False)
	telefono = models.CharField('Teléfono', max_length = 15, blank = False, null = False)	
	
	class Meta:
		abstract = True


class Cliente(Persona):
	edad = models.IntegerField('Edad', blank = False, null = False)
	direccion = models.CharField('Dirección', max_length = 50, blank = False, null = False)
	
	def __str__(self):
		return self.documento_id