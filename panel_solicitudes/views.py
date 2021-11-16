from django.db.models.fields import DateField
from django.http import request
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.utils import timezone
from .forms import *
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

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
            user = form.cleaned_data.get('username')
            messages.success(request, 'Cuenta fue creada' + user)
            return redirect('login')

    context = {'form': form}

    return render(request, 'panel_solicitudes/templates/registrar.html', context)

def login_pagina(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Apodo o Contraseña incorrectos')
            
    context = {}
    
    return render(request, 'panel_solicitudes/templates/login.html', context )

def logout_usuario(request):
    logout(request)
    return redirect('login')


def categorias_lista(request):
    categorias = Categoria.objects.order_by('nombre')
    return render(request, 'panel_solicitudes/templates/categorias_lista.html', {'categorias': categorias} )


# Pagina para listar los Maestros
def maestros_lista(request):
    maestros = PerfilMaestro.objects.order_by('id')
    return render(request, 'panel_solicitudes/templates/maestros_lista.html', {'maestros': maestros})


def maestro_solicitudes(request, pk):
    #perfil_maestro = get_object_or_404(PerfilMaestro, pk=pk)
    #perfilmaestro = PerfilMaestro.objects.get('pk')

    #solicitud = SolicitudTarea.objects.order_by('pk')
    #solicitudes = SolicitudTarea.objects.get('pk')
    


    #AL PARECER QUEDO FUNCIONANDO BIEN EL FILTRADO
    solicitudes = SolicitudTarea.objects.filter(perfil_maestro_id = pk)
    #solicitudes = SolicitudTarea.objects.all().filter(perfil_maestro == request.pk)

    
    # ESTE FUNCIONA
    #solicitudes = SolicitudTarea.objects.order_by('pk')
    return render(request, 'maestro_solicitudes.html', {'solicitudes': solicitudes})

def maestro_detalle(request, pk):
    maestro = get_object_or_404(PerfilMaestro, pk=pk)
    return render(request, 'maestro_detalle.html', {'maestro': maestro})

def maestro_nueva(request):
    if request.method == "POST":
        form = MaestroForm(request.POST)
        # Con esto obtenemos todos los datos del usuario actual
        mi_usuario = Usuario.objects.get(user=request.user)
        if form.is_valid():
            maestro = form.save(commit=False)
            # Estas lineas de codigo pueden arreglar errores futuros
            maestro.usuario = mi_usuario
            maestro.created_date = timezone.now()
            maestro.save()
            form.save_m2m()
            return redirect('maestro_detalle', pk=maestro.pk)
    else:
        form = MaestroForm()
    return render(request, 'maestro_editar.html', {'form': form})


def maestro_editar(request, pk):
    maestro = get_object_or_404(PerfilMaestro, pk=pk)
    if request.method == "POST":
        form = MaestroForm(request.POST, instance=maestro)
        # Con esto obtenemos todos los datos del usuario actual
        mi_usuario = Usuario.objects.get(user=request.user)
        if form.is_valid():
            maestro = form.save(commit=False)
            # Estas lineas de codigo pueden arreglar errores futuros
            maestro.usuario = mi_usuario
            maestro.created_date = timezone.now()
            maestro.save()
            form.save_m2m()
            return redirect('maestro_detalle', pk=maestro.pk)
    else:
        form = MaestroForm(instance=maestro)
    return render(request, 'maestro_editar.html', {'form': form})








def solicitud_lista(request):
    solicitud_tareas = SolicitudTarea.objects.order_by('id')
    return render(request, 'solicitud_tareas.html', {'solicitud_tareas':solicitud_tareas})

def solicitud_detalle(request, pk):
    solicitud_tarea = get_object_or_404(SolicitudTarea, pk=pk)
    return render(request, 'solicitud_detalle.html', {'solicitud_tarea': solicitud_tarea})

def solicitud_nueva(request):
    if request.method == "POST":
        form = Solicitud_Tarea_Form(request.POST)
        if form.is_valid():
            solicitud_tarea = form.save(commit=False)
            solicitud_tarea.author = request.user
            solicitud_tarea.created_date = timezone.now()
            solicitud_tarea.save()
            return redirect('solicitud_detalle', pk=solicitud_tarea.pk)
    else:
        form = Solicitud_Tarea_Form()
    return render(request, 'solicitud_editar.html', {'form': form})

def solicitud_editar(request, pk):
    post = get_object_or_404(SolicitudTarea, pk=pk)
    if request.method == "POST":
        form = Solicitud_Tarea_Form(request.POST, instance=post)
        if form.is_valid():
            solicitud_tarea = form.save(commit=False)
            solicitud_tarea.author = request.user
            solicitud_tarea.created_date = timezone.now()
            solicitud_tarea.save()
            return redirect('solicitud_detalle', pk=solicitud_tarea.pk)
    else:
        form = Solicitud_Tarea_Form(instance=post)
    return render(request, 'solicitud_editar.html', {'form': form})





def usuario_lista(request):
    usuarios = Usuario.objects.order_by('id')
    return render(request, 'usuario_lista.html', {'usuarios':usuarios})

def usuario_detalle(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    return render(request, 'usuario_detalle.html', {'usuario': usuario})

def usuario_nueva(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.user = request.user
            usuario.created_date = timezone.now()
            usuario.save()
            return redirect('usuario_detalle', pk=usuario.pk)
    else:
        form = UsuarioForm()
    return render(request, 'usuario_editar.html', {'form': form})


def usuario_editar(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == "POST":
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.user = request.user
            usuario.created_date = timezone.now()
            usuario.save()
            return redirect('usuario_detalle', pk=usuario.pk)
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'usuario_editar.html', {'form': form})


