from django import forms

from .models import Cliente, Persona

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['rif',]