from django.db import models
from django.utils import timezone
# Create your models here.
from django.contrib.auth.models import User

class Comuna(models.Model):
    nombre = models.TextField()

    def __str__(self):
        return self.nombre

class Genero(models.Model):
    nombre = models.TextField()

    def __str__(self):
        return self.nombre

class TipoUsuario(models.Model):
    nombre = models.TextField()

    def __str__(self):
        return self.nombre

class Verificacion(models.Model):
    nombre = models.TextField()

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.TextField()
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


    #   Unirlas a las categorias 
    #   Unir las Tareas a Oficio
    #   Crear Tareas
class Tarea(models.Model):
    nombre = models.TextField()
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

    #   
    #   Oficios es el Conjunto de las tareas que puede hacer un Maestro
    #   Por lo tanto es creado por los Usuarios
    #
class Oficio(models.Model):
    nombre = models.TextField()

    def __str__(self):
        return self.nombre


class Estado(models.Model):
    nombre = models.TextField()

    def __str__(self):
        return self.nombre

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class Usuario(models.Model):
    nombre = models.TextField()
    apellidos = models.TextField()
    rut = models.TextField()
    fecha_nacimiento = models.DateField()
    direccion = models.TextField()
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    verificacion = models.ForeignKey(Verificacion, on_delete=models.CASCADE)
    created_date = models.DateTimeField(
        default=timezone.now)

    def __str__(self):
        return "%s %s %s %s" % (self.rut, self.nombre, self.apellidos, self.verificacion)

    #
    #
    #
    #
    #
class Fotos(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, blank=True, null=True)
    upload = models.FileField(upload_to=user_directory_path)
    def __str__(self):
        return "%s %s %s" % (self.usuario.nombre, self.usuario.apellidos, self.usuario.rut)
        #return self.usuario.rut
 
class PerfilMaestro(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, blank=True, null=True)
    created_date = models.DateTimeField(
        default=timezone.now)

    def __str__(self):
        return "%s %s %s" % (self.usuario.nombre, self.usuario.apellidos, self.usuario.rut)

class SolicitudTarea(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    perfil_maestro = models.ForeignKey(PerfilMaestro, on_delete=models.CASCADE)
    nombre = models.TextField()
    tarea = models.TextField()
    descripcion = models.TextField()
    direccion = models.TextField()
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    created_date = models.DateTimeField(
        default=timezone.now)
    fecha = models.DateTimeField()
    def __str__(self):
        return "%s %s %s %s" % (self.nombre, self.tarea, self.direccion, self.estado)


