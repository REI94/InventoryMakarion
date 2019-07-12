from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser, UserManager

class CustomUserManager(UserManager):
    pass


class CustomUser(AbstractUser):
    objects = CustomUserManager()


class CompleteUser(CustomUser):
    cedula = models.CharField('Cédula', max_length=10, primary_key=True,
    help_text="Ejemplo: V011223318",
    validators=[RegexValidator(regex="^[V|E]{1}[0]{1}[0-9]{7,9}$",
    message="Cédula ingresada incorrectamente, debe ingresarla nuevamente.")])
    edad = models.IntegerField()
    direccion = models.TextField('Dirección')
    telefono = models.CharField('Teléfono', max_length=12)