from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

from .models import CompleteUser


class CustomUserCreationForm(UserCreationForm):
	
	class Meta(UserCreationForm.Meta):
		model = CompleteUser
		fields = (
			'username',
			'first_name',
			'last_name',
			'cedula',
			'edad',
			'direccion' ,
			'telefono' ,
			'email' ,        
		)
		
		labels = dict(username='Nombre de usuario', first_name='Nombre',
			last_name='Apellidos',cedula='Cédula de identidad', edad= 'Edad', 
            direccion='Dirección', telefono='Número de teléfono', 
            email='Correo electrónico')

		widgets = {
			'direccion': forms.Textarea(attrs={'rows': 3}),
		}
		

class CustomUserChangeForm(UserChangeForm):
	class Meta:
		model = CompleteUser
		fields = UserChangeForm.Meta.fields