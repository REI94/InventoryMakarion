from django import forms

from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            'codigo',
            'precio',
            'tipo',
            'cantidad',
            'categoria',
        ]

        labels = {
            'codigo': 'Codigo',
            'precio': 'Precio',
            'tipo': 'Tipo',
            'cantidad': 'Cantidad',
            'categoria': 'Categoria',
        }

        widgets = {
            'codigo': forms.TextInput(attrs={'class':'form-control'}),
            'precio': forms.TextInput(attrs={'class':'form-control'}),
            'tipo': forms.TextInput(attrs={'class':'form-control'}),
            'cantidad': forms.TextInput(attrs={'class':'form-control'}),
            'categoria': forms.Select(attrs={'class':'form-control'}),
        }
        

