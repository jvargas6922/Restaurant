from django.db import models
from apps.categorias.models import Categoria
from django.utils import timezone

# Create your models here.
class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock_disponible = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, db_column='id_categoria')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'productos'

    def delete(self):
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        self.deleted_at = None
        self.save()

    def __str__(self):
        return self.nombre



