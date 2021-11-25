from django.core.exceptions import PermissionDenied
from .models import *
from django.shortcuts import get_object_or_404


def user_is_entry_author(function):
    def wrap(request, *args, **kwargs):

        usuario = Usuario.objects.get(pk=kwargs['pk'])
        if usuario.user == request.user:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


def user_is_master_author(function):
    def wrap(request, *args, **kwargs):

        maestro = PerfilMaestro.objects.get(pk=kwargs['pk'])
        if maestro.author == request.user:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap

def user_is_solicitud_author(function):
    def wrap(request, *args, **kwargs):

        solicitud = SolicitudTarea.objects.get(pk=kwargs['pk'])
        if solicitud.author == request.user:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap

def user_has_usuario(function):
    def wrap(request, *args, **kwargs):
        #usuario = get_object_or_404(Usuario, pk=pk)
        mi_usuario = User.objects.get(id=request.user.id)
        usuario = Usuario.objects.get(pk=kwargs['mi_usuario'])
        
        if Usuario.objects.get(user=request.mi_usuario).exists():
            #return function(request, *args, **kwargs)
            raise PermissionDenied
        else:
            #raise PermissionDenied
            return function(request, *args, **kwargs)
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap