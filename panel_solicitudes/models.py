from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator

# Create your models here.
from django.contrib.auth.models import User

class Comuna(models.Model):
    nombre = models.TextField(max_length=50)

    def __str__(self):
        return self.nombre

class Calificacion(models.Model):
    estrellas = models.TextField()

    def __str__(self):
        return str(self.estrellas)

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
        return "%s %s" % (self.id, self.nombre)


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
    nombre = models.TextField(default='Pepe', max_length=50)
    apellidos = models.TextField(default='Perez', max_length=50)
    # user es el author en otros modelos pero para mantener nombre dentro del usuario quedo asi
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    rut = models.TextField(max_length=12)
    fecha_nacimiento = models.DateField()
    direccion = models.TextField(max_length=100)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, default=1)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    verificacion = models.ForeignKey(Verificacion, on_delete=models.CASCADE, default=1)
    created_date = models.DateTimeField(
        default=timezone.now)
    celular = models.TextField(default='+56977777777', max_length=12)
    
    def __str__(self):
        return "%s %s %s %s %s %s %s" % (self.rut, self.user, self.nombre, self.apellidos, self.direccion, self.fecha_nacimiento, self.celular)

    #
    #

class Foto(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, blank=True, null=True)
    upload = models.FileField(upload_to=user_directory_path)
    
    def __str__(self):
        return "%s %s %s" % (self.usuario.nombre, self.usuario.apellidos, self.usuario.rut)
        #return self.usuario.rut
 
class PerfilMaestro(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, default=1)
    #   EL CAMPO USUARIO PUEDE SER QUE ESTE DE MAS Y TIRANDO ERRORES
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, blank=True, null=True)
    #   Creacion de la relacion de los perfiles de maestros a las tareas que pueden ejecutar
    tareas = models.ManyToManyField(Tarea)
    created_date = models.DateTimeField(
        default=timezone.now)

    def __str__(self):
        return "%s %s" % (self.usuario, list(self.tareas.all()))

class SolicitudTarea(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, default=1)
    #                                                   related_name='solicitudtarea'
    perfil_maestro = models.ForeignKey('PerfilMaestro', on_delete=models.CASCADE, related_name='solicitudtarea')
    nombre = models.TextField(max_length=50)
    tarea = models.TextField(max_length=250)
    descripcion = models.TextField(max_length=250)
    direccion = models.TextField(max_length=250)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, default=1)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, default=1)
    # Agregar Calificacion
    calificacion = models.ForeignKey(Calificacion, on_delete=models.CASCADE, default=4)
    created_date = models.DateTimeField(
        default=timezone.now)
    fecha = models.DateField()
    def __str__(self):
        return "%s %s %s %s %s" % (self.nombre, self.tarea, self.direccion, self.estado, self.perfil_maestro)


class ComentarioSolicitud(models.Model):
    #                              panel_solicitudes.SolicitudTarea
    solicitud = models.ForeignKey('SolicitudTarea', on_delete=models.CASCADE, related_name='comentariossolicitud')
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, default=1)
    text = models.TextField(max_length=250)
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)
    
    def approve(self):
        self.approved_comment = True
        self.save()
    def __str__(self):
        return self.text

class ComentarioMaestro(models.Model):
    #                              panel_solicitudes.PerfilMaestro
    maestro = models.ForeignKey('PerfilMaestro', on_delete=models.CASCADE, related_name='comentariosmaestro')
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, default=1)
    text = models.TextField(max_length=250)
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)
    
    def approve(self):
        self.approved_comment = True
        self.save()
    def __str__(self):
        return self.text


class Sugerencia(models.Model):
    descripcion = models.TextField(max_length=250)
    # Agregar el Author de la sugerencia para futuras posibles notificaciones
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, default=1)
    def __str__(self):
        return "%s %s" % (self.descripcion, self.author)