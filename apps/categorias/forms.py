from django import forms
from .models import Categoria

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ingrese el nombre de la categoría'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control','placeholder': 'Ingrese una descripción para la categoría', 'rows': 3}),
        }