from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from apps.categorias.models import Categoria
from .forms import ProductoForm

# Create your views here.
def productos_por_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id_categoria=categoria_id)
    productos = Producto.objects.filter(categoria_id=categoria_id, deleted_at__isnull=True)
    context = {
        'productos': productos,
        'categoria': categoria,
    }
    return render(request, 'productos/productos_por_categoria.html', context)

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('productos-por-categoria', categoria_id=form.cleaned_data['categoria'].id_categoria)
    else:
        form = ProductoForm()
        context ={
            'form': form,
        }
    return render(request, 'productos/crear_producto.html', context)

def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id_producto=producto_id)
    form = ProductoForm(instance=producto)
    context = {
        "form": form,
    }
    return render(request, 'productos/editar_producto.html', context)

