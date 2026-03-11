from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('core/contador_visitas/', views.contador_visitas, name='contador-visitas'),
]