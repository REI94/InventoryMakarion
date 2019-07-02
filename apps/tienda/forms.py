from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre','apellido','tipo_documento_id','num_documento_id','edad','telefono','direccion','email','contrasenia']