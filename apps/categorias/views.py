from django.shortcuts import render, redirect, get_object_or_404
from .models import Categoria
from .forms import CategoriaForm
# Create your views here.

def index(request):
    """
    id_categoria = Categoria.objects.filter(deleted_at__isnull=False)
    if id_categoria:
        for categoria in id_categoria:
            restaurar_categoria(categoria.id_categoria)
    """
    categorias = Categoria.objects.filter(deleted_at__isnull=True)
    context = {
        'categorias': categorias,
    }
    return render(request, 'categorias/index.html', context)

def crear_categoria(request):
    try:
        if request.method == 'POST':
            form = CategoriaForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('listado-categorias')
        else:
            form = CategoriaForm()
    except Exception as e:
        form = CategoriaForm()
        print(f"Error al crear categoría: {e}")
    form = CategoriaForm()
    context = {
        'form': form,
    }
    return render(request, 'categorias/crear_categoria.html', context)

def editar_categoria(request, id_categoria):
    try:
        categoria = get_object_or_404(Categoria, id_categoria=id_categoria)
        form = CategoriaForm(instance=categoria)
        context ={
            'form': form,
            'categoria': categoria,
        }
    except Exception as e:
        print(f"Error al obtener categoría: {e}")
    return render(request, 'categorias/editar_categoria.html', context)

def actualizar_categoria(request, id_categoria):
    try:
        categoria = get_object_or_404(Categoria, id_categoria=id_categoria)
        if request.method == 'POST':
            form = CategoriaForm(request.POST, instance=categoria)
            if form.is_valid():
                form.save()
                return redirect('listado-categorias')
        else:
            form = CategoriaForm(instance=categoria)
    except Exception as e:
        print(f"Error al actualizar categoría: {e}")
        form = CategoriaForm(instance=categoria)
    context = {
        'form': form,
        'categoria': categoria,
    }
    return render(request, 'categorias/editar_categoria.html', context)

def eliminar_categoria(request, id_categoria):
    try:
        categoria = get_object_or_404(Categoria, id_categoria=id_categoria)
        print(categoria)
        categoria.delete()
    except Exception as e:
        print(f"Error al eliminar categoría: {e}")
    return redirect('listado-categorias')

def restaurar_categoria(id_categoria):
    try:
        categoria = get_object_or_404(Categoria, id_categoria=id_categoria)
        categoria.restore()
    except Exception as e:
        print(f"Error al restaurar categoría: {e}")
