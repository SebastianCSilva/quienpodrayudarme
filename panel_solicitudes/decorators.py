from django.core.exceptions import PermissionDenied
from .models import *

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