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

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellidos', 'rut', 'fecha_nacimiento', 'direccion', 'genero','celular']
        widgets = {
            'fecha_nacimiento': DateInput(format=('%Y-%m-%d')),
        }

class MaestroForm(forms.ModelForm):
    class Meta:
        model = PerfilMaestro
        fields = ['tareas']
        
    tareas = forms.ModelMultipleChoiceField(
            queryset=Tarea.objects.all(),
            widget=forms.CheckboxSelectMultiple
    )

class ComentarioSolicitudForm(forms.ModelForm):
    class Meta:
        model = ComentarioSolicitud
        fields = ['text']

class ComentarioMaestroForm(forms.ModelForm):
    class Meta:
        model = ComentarioMaestro
        fields = ['text']

class Solicitud_Maestro_Tarea_Form(forms.ModelForm):
    class Meta:
        model = SolicitudTarea
        fields = ['nombre', 'tarea', 'descripcion', 'direccion', 'estado','fecha']
        widgets = {
            'fecha': DateInput(format=('%Y-%m-%d')),
        }

