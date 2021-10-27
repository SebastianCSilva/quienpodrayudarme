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
        return "%s %s %s" % (self.id, self.nombre, self.descripcion)


class Tarea(models.Model):
    nombre = models.TextField()
    descripcion = models.TextField()
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return "%s %s %s %s" % (self.id, self.nombre, self.descripcion, self.id_categoria)


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

class Foto(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, blank=True, null=True)
    upload = models.FileField(upload_to=user_directory_path)
    
    def __str__(self):
        return "%s %s %s" % (self.usuario.nombre, self.usuario.apellidos, self.usuario.rut)
        #return self.usuario.rut
 
class PerfilMaestro(models.Model):

    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    #   EL CAMPO USUARIO PUEDE SER QUE ESTE DE MAS Y TIRANDO ERRORES
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, blank=True, null=True)
    #   Creacion de la relacion de los perfiles de maestros a las tareas que pueden ejecutar
    tareas = models.ManyToManyField(Tarea, blank=True)

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


