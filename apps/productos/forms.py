from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'stock_disponible', 'categoria']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ingrese el nombre del producto'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Ingrese el precio del producto'}),
            'stock_disponible': forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Ingrese el stock disponible del producto','min': 1}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
        }