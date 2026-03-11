from django.contrib import admin
from .models import Producto

# Register your models here.

"""
1)SOLO REGISTRA MI MODELO EN EL PANEL DE ADMINISTRACION
"""
# admin.site.register(Producto)

"""
2 ) PERSONALIZAR EL PANEL DE ADMINISTRACION PARA MI MODELO
"""
class ProductoAdmin(admin.ModelAdmin):
    # Campos que se mostrarán en la lista de productos
    list_display = ('nombre', 'precio', 'categoria')
    # Campos por los que se puede buscar
    search_fields = ('nombre',)
    # Filtros para la barra lateral
    list_filter = ('categoria','precio') 

admin.site.register(Producto, ProductoAdmin)