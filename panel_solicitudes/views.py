from django.http import request
from django.shortcuts import render
from .models import *
from django.utils import timezone
from .forms import *
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate, login as dj_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
# Pagina de Bienvenida para los usuarios nuevos
def home(request):
    return render(request, 'panel_solicitudes/templates/home.html', {} )

def registrar(request):
    form = UsuarioCreacionForm()

    if request.method == 'POST':
        form = UsuarioCreacionForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}

    return render(request, 'panel_solicitudes/templates/registrar.html', context)

def login(request):
    return render(request, 'panel_solicitudes/templates/login.html', {} )

# Pagina para listar los Maestros
def maestros_lista(request):
    return render(request, 'panel_solicitudes/templates/maestros_lista.html', {})


def categorias_lista(request):
    categorias = Categoria.objects.order_by('nombre')
    return render(request, 'panel_solicitudes/templates/categorias_lista.html', {'categorias': categorias} )

