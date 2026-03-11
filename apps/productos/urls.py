from django.urls import path
from . import views

urlpatterns = [
    path('productos_por_categoria/<int:categoria_id>/', views.productos_por_categoria, name='productos-por-categoria'),
    path('crear_producto/', views.crear_producto, name='crear-producto'),
    path('editar_producto/<int:producto_id>/', views.editar_producto, name='editar-producto'),
]