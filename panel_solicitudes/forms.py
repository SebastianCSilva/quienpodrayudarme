from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DateInput(forms.DateInput):
    input_type = 'date'


class UsuarioCreacionForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class Solicitud_Tarea_Form(forms.ModelForm):

    class Meta:
        model = SolicitudTarea
        fields = ('perfil_maestro', 'nombre', 'tarea', 'descripcion', 'direccion','estado','fecha')
        widgets = {
            'fecha': DateInput(format=('%Y-%m-%d')),
        }