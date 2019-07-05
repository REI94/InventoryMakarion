from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Cliente, Persona

class ClienteForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',                       
        ]
        labels = {
            'username': 'Nombre de usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo electrónico',
        }