from django import forms

from .models import Cliente, Persona

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre','apellido','tipo_documento_id','documento_id','edad','telefono','direccion','email','contrasenia']