from django import forms

from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            'codigo',
            'nombre',
            'precio',
            'descripcion',
            'cantidad',
            'categoria',
        ]

        labels = {
            'codigo': 'Codigo',
            'nombre': 'Nombre',
            'precio': 'Precio',
            'descripcion': 'Descripcion',
            'cantidad': 'Cantidad',
            'categoria': 'Categoria',
        }

        widgets = {
            'codigo': forms.TextInput(attrs={'class':'form-control'}),
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'precio': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.TextInput(attrs={'class':'form-control'}),
            'cantidad': forms.TextInput(attrs={'class':'form-control'}),
            'categoria': forms.Select(attrs={'class':'form-control'}),
        }
        

