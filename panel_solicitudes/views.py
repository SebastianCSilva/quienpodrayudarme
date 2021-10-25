from django.shortcuts import render
from .models import *
from django.utils import timezone

# Create your views here.
# Pagina de Bienvenida para los usuarios nuevos
def home(request):
    return render(request, 'panel_solicitudes/templates/home.html', {} )


# Pagina para listar los Maestros
def maestros_lista(request):
    return render(request, 'panel_solicitudes/templates/maestros_lista.html', {})


def categorias_lista(request):
    categorias = Categoria.objects.order_by('nombre')
    return render(request, 'panel_solicitudes/templates/categorias_lista.html', {'categorias': categorias} )

