from django.db.models.fields import DateField
from django.http import request
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.utils import timezone
from django.core.paginator import Paginator

from .forms import *
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import *


# Create your views here.
# Pagina de Bienvenida para los usuarios nuevos
def home(request):
    return render(request, 'panel_solicitudes/templates/home.html', {} )

def rutas(request):
    return render(request, 'panel_solicitudes/templates/rutas.html', {} )

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

def tareas_lista(request):
    tareas = Tarea.objects.order_by('nombre')
    return render(request, 'panel_solicitudes/templates/tareas_lista.html', {'tareas': tareas} )

def tarea_maestros(request, pk):
    maestros = PerfilMaestro.objects.filter(tareas=pk).order_by('-created_date')
    return render(request, 'tarea_maestros.html', {'maestros': maestros})



# Pagina para listar los Maestros
def maestros_lista(request):
    maestros = PerfilMaestro.objects.order_by('-created_date')
    # Probando codigo de paginacion
    paginator = Paginator(maestros, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # Funcionando
    return render(request, 'panel_solicitudes/templates/maestros_lista.html', {'page_obj': page_obj})




@login_required(login_url='/login')
def maestro_solicitudes(request, pk):
    #perfil_maestro = get_object_or_404(PerfilMaestro, pk=pk)
    #perfilmaestro = PerfilMaestro.objects.get('pk')

    #solicitud = SolicitudTarea.objects.order_by('pk')
    #solicitudes = SolicitudTarea.objects.get('pk')
    


    #AL PARECER QUEDO FUNCIONANDO BIEN EL FILTRADO
    solicitudes = SolicitudTarea.objects.filter(perfil_maestro_id = pk).order_by('-created_date')
    #solicitudes = SolicitudTarea.objects.all().filter(perfil_maestro == request.pk)

    
    # ESTE FUNCIONA
    #solicitudes = SolicitudTarea.objects.order_by('pk')
    return render(request, 'maestro_solicitudes.html', {'solicitudes': solicitudes})

@login_required(login_url='/login')
def maestro_detalle(request, pk):
    maestro = get_object_or_404(PerfilMaestro, pk=pk)
    return render(request, 'maestro_detalle.html', {'maestro': maestro})

@login_required(login_url='/login')
def maestro_nueva(request):
    if request.method == "POST":
        form = MaestroForm(request.POST)
        # Con esto obtenemos todos los datos del usuario actual
        # mi_usuario = User.objects.get(id=request.user.id)
        mi_usuario = Usuario.objects.get(user=request.user)
        mi_usuario2 = User.objects.get(id=request.user.id)
        if form.is_valid():
            maestro = form.save(commit=False)
            # Estas lineas de codigo pueden arreglar errores futuros
            maestro.usuario = mi_usuario
            maestro.author = mi_usuario2
            maestro.created_date = timezone.now()
            maestro.save()
            form.save_m2m()
            return redirect('maestro_detalle', pk=maestro.pk)
    else:
        form = MaestroForm()
    return render(request, 'maestro_editar.html', {'form': form})

@login_required(login_url='/login')
@user_is_master_author
def maestro_editar(request, pk):
    maestro = get_object_or_404(PerfilMaestro, pk=pk)
    if request.method == "POST":
        form = MaestroForm(request.POST, instance=maestro)
        # Con esto obtenemos todos los datos del usuario actual
        mi_usuario = Usuario.objects.get(user=request.user)
        mi_usuario2 = User.objects.get(id=request.user.id)
        if form.is_valid():
            maestro = form.save(commit=False)
            # Estas lineas de codigo pueden arreglar errores futuros
            maestro.usuario = mi_usuario
            maestro.author = mi_usuario2
            maestro.created_date = timezone.now()
            maestro.save()
            form.save_m2m()
            return redirect('maestro_detalle', pk=maestro.pk)
    else:
        form = MaestroForm(instance=maestro)
    return render(request, 'maestro_editar.html', {'form': form})






#Agregar paginacion
@login_required(login_url='/login')
def solicitud_lista(request):
    solicitud_tareas = SolicitudTarea.objects.order_by('-id')
    """
        paginator = Paginator(maestros, 12)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    """
    paginator = Paginator(solicitud_tareas, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'solicitud_tareas.html', {'page_obj':page_obj})

@login_required(login_url='/login')
def solicitud_detalle(request, pk):
    solicitud_tarea = get_object_or_404(SolicitudTarea, pk=pk)
    return render(request, 'solicitud_detalle.html', {'solicitud_tarea': solicitud_tarea})

@login_required(login_url='/login')
def solicitud_nueva(request):
    if request.method == "POST":
        form = Solicitud_Tarea_Form(request.POST)
        # mi_usuario = Usuario.objects.get(user=request.user)
        # mi_usuario2 = User.objects.get(id=request.user.id)
        mi_usuario = User.objects.get(id=request.user.id)
        if form.is_valid():
            solicitud_tarea = form.save(commit=False)
            solicitud_tarea.author = mi_usuario
            solicitud_tarea.created_date = timezone.now()
            solicitud_tarea.save()
            return redirect('solicitud_detalle', pk=solicitud_tarea.pk)
    else:
        form = Solicitud_Tarea_Form()
    return render(request, 'solicitud_editar.html', {'form': form})

@login_required(login_url='/login')
@user_is_solicitud_author
def solicitud_editar(request, pk):
    post = get_object_or_404(SolicitudTarea, pk=pk)
    if request.method == "POST":
        form = Solicitud_Tarea_Form(request.POST, instance=post)
        mi_usuario = Usuario.objects.get(user=request.user)
        if form.is_valid():
            solicitud_tarea = form.save(commit=False)
            solicitud_tarea.author = mi_usuario
            solicitud_tarea.created_date = timezone.now()
            solicitud_tarea.save()
            return redirect('solicitud_detalle', pk=solicitud_tarea.pk)
    else:
        form = Solicitud_Tarea_Form(instance=post)
    return render(request, 'solicitud_editar.html', {'form': form})




@login_required(login_url='/login')
def usuario_lista(request):
    usuarios = Usuario.objects.order_by('id')
    paginator = Paginator(usuarios, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'usuario_lista.html', {'page_obj':page_obj})

@login_required(login_url='/login')
@user_is_entry_author
def usuario_detalle(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    return render(request, 'usuario_detalle.html', {'usuario': usuario})

@login_required(login_url='/login')
def usuario_nueva(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        mi_usuario = User.objects.get(id=request.user.id)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.user = mi_usuario
            #usuario.author = mi_usuario
            usuario.created_date = timezone.now()
            usuario.save()
            return redirect('usuario_detalle', pk=usuario.pk)
    else:
        form = UsuarioForm()
    return render(request, 'usuario_editar.html', {'form': form})

@login_required(login_url='/login')
@user_is_entry_author
def usuario_editar(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == "POST":
        form = UsuarioForm(request.POST, instance=usuario)
        mi_usuario = User.objects.get(id=request.user.id)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.user = mi_usuario
            usuario.created_date = timezone.now()
            usuario.save()
            return redirect('usuario_detalle', pk=usuario.pk)
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'usuario_editar.html', {'form': form})

    """
        mi_usuario = Usuario.objects.get(user=request.user.id)
        mi_usuario2 = User.objects.get(id=request.user.id)
    
    """



        # mi_usuario = Usuario.objects.get(user=request.user)
        # mi_usuario2 = User.objects.get(id=request.user.id)

@login_required(login_url='/login')
def mis_usuarios(request):
    #mi_usuario = Usuario.objects.get(user=request.user)
    usuarios = Usuario.objects.filter(user_id = request.user.id)
    return render(request, 'mis_usuarios.html', {'usuarios':usuarios})
    

@login_required(login_url='/login')
def mis_maestros(request):
    maestros = PerfilMaestro.objects.filter(author_id = request.user.id).order_by('-created_date')
    paginator = Paginator(maestros, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'mis_maestros.html', {'page_obj':page_obj})

    
@login_required(login_url='/login')
def mis_solcitudes(request):
    
    solicitudes = SolicitudTarea.objects.filter(author_id = request.user.id).order_by('-created_date')
    paginator = Paginator(solicitudes, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'mis_solcitudes.html', {'page_obj':page_obj})


def agregar_comentario_solicitud(request, pk):
    solicitud = get_object_or_404(SolicitudTarea, pk=pk)
    if request.method == "POST":
        form = ComentarioSolicitudForm(request.POST)
        mi_usuario = User.objects.get(id=request.user.id)
        if form.is_valid():
            comentariossolicitud = form.save(commit=False)
            comentariossolicitud.solicitud = solicitud
            comentariossolicitud.author = mi_usuario
            comentariossolicitud.save()
            return redirect('solicitud_detalle', pk=solicitud.pk)
    else:
        form = ComentarioSolicitudForm()
    return render(request, 'agregar_comentario_solicitud.html', {'form': form})

def agregar_comentario_maestro(request, pk):
    maestro = get_object_or_404(PerfilMaestro, pk=pk)
    if request.method == "POST":
        form = ComentarioMaestroForm(request.POST)
        mi_usuario = User.objects.get(id=request.user.id)
        if form.is_valid():
            comentariosmaestro = form.save(commit=False)
            comentariosmaestro.maestro = maestro
            comentariosmaestro.author = mi_usuario
            comentariosmaestro.save()
            return redirect('maestro_detalle', pk=maestro.pk)
    else:
        form = ComentarioSolicitudForm()
    return render(request, 'agregar_comentario_maestro.html', {'form': form})

@login_required(login_url='/login')
def agregar_solicitud_nueva(request, pk):
    maestro = get_object_or_404(PerfilMaestro, pk=pk)
    if request.method == "POST":
        form = Solicitud_Maestro_Tarea_Form(request.POST)
        mi_usuario = User.objects.get(id=request.user.id)
        if form.is_valid():
            solicitud_tarea = form.save(commit=False)
            solicitud_tarea.author = mi_usuario
            solicitud_tarea.perfil_maestro = maestro
            solicitud_tarea.created_date = timezone.now()
            solicitud_tarea.save()
            return redirect('solicitud_detalle', pk=solicitud_tarea.pk)
    else:
        form = Solicitud_Maestro_Tarea_Form()
    return render(request, 'agregar_solicitud_nueva.html', {'form': form})

@login_required(login_url='/login')
@user_is_solicitud_author
def solicitud_editar_nueva(request, pk):
    post = get_object_or_404(SolicitudTarea, pk=pk)
    if request.method == "POST":
        form = Solicitud_Maestro_Tarea_Form(request.POST, instance=post)
        mi_usuario = Usuario.objects.get(user=request.user.id)
        mi_usuario2 = User.objects.get(id=request.user.id)
        if form.is_valid():
            solicitud_tarea = form.save(commit=False)
            solicitud_tarea.author = mi_usuario2
            solicitud_tarea.created_date = timezone.now()
            solicitud_tarea.save()
            return redirect('solicitud_detalle', pk=solicitud_tarea.pk)
    else:
        form = Solicitud_Maestro_Tarea_Form(instance=post)
    return render(request, 'solicitud_editar.html', {'form': form})

def busqueda_tareas(request):
    if request.method == "POST":
        searched  = request.POST.get('searched')
        tareas = Tarea.objects.filter(nombre__icontains=searched)
        return render(request, 'busqueda_tareas.html', {'searched':searched,
        'tareas':tareas})
    else:
        render(request, 'busqueda_tareas.html', {})
    

def comunas_lista(request):
    comunas = Comuna.objects.order_by('nombre')
    return render(request, 'panel_solicitudes/templates/comunas_lista.html', {'comunas': comunas} )


def comunas_maestros(request, pk):
    maestros = PerfilMaestro.objects.filter(usuario__comuna=pk)
    return render(request, 'comunas_maestros.html', {'maestros': maestros})
#
#
#
@login_required(login_url='/login')
def agregar_sugerencia(request):
    if request.method == "POST":
        form = SugerenciaForm(request.POST)
        mi_usuario = User.objects.get(id=request.user.id)
        if form.is_valid():
            sugerencia = form.save(commit=False)
            sugerencia.author = mi_usuario
            sugerencia.created_date = timezone.now()
            sugerencia.save()
            return redirect('home')
    else:
        form = SugerenciaForm()
    return render(request, 'agregar_sugerencia.html', {'form': form})