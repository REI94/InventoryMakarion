from django import forms

from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            'codigo',
            'nombre',
            'categoria',
            'precio',
            'precio_en_descuento',
            'descripcion',
            'cantidad',
            'disponible',
            'unidades_vendidas',
            'texto_destacado',
            'caracteristica_destacada',            
        ]

        labels = {
            'codigo': 'Código',
            'nombre': 'Nombre',
            'categoria': 'Categoría',            
            'precio': 'Precio',
            'precio_en_descuento': 'Precio en descuento',
            'descripcion': 'Descripción',
            'cantidad': 'Cantidad',
            'disponible': 'Disponible',
            'unidades_vendidas': 'Unidades vendidas',
            'texto_destacado': 'Texto destacado',
            'caracteristica_destacada': 'Característica destacada',
            'imagen': 'Imágen destacada',
        }

        widgets = {
            'codigo': forms.TextInput(attrs={'class':'form-control'}),
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'categoria': forms.Select(attrs={'class':'form-control'}),
            'precio': forms.TextInput(attrs={'class':'form-control'}),
            'precio_en_descuento': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.TextInput(attrs={'class':'form-control'}),
            'cantidad': forms.TextInput(attrs={'class':'form-control'}),
            'disponible': forms.TextInput(attrs={'class':'form-control'}),
            'unidades_vendidas': forms.TextInput(attrs={'class':'form-control'}),
            'texto_destacado': forms.TextInput(attrs={'class':'form-control'}),
            'caracteristica_destacada': forms.TextInput(attrs={'class':'form-control'}),        
        }