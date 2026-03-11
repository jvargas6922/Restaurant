from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='listado-categorias'),
    path('crear/', views.crear_categoria, name='crear-categoria'),
    path('editar/<int:id_categoria>/', views.editar_categoria, name='editar-categoria'),
    path('actualizar/<int:id_categoria>/', views.actualizar_categoria, name='actualizar-categoria'),
    path('eliminar/<int:id_categoria>/', views.eliminar_categoria, name='eliminar-categoria'),
]