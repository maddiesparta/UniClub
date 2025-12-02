from django.contrib.auth.models import AbstractUser
from django.db import models

class Evento(models.Model):
    titulo = models.CharField(max_length=100, unique=True)
    descripcion = models.CharField(max_length=300)
    fecha= models.CharField(max_length=15)
    pancarta= models.URLField(max_length=200)
    tematica= models.CharField(max_length=20)
    organizador = models.ForeignKey('Organizador', on_delete=models.CASCADE, related_name='organizador')

    def __str__(self):
        return self.titulo
    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"

class Actividad(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=300)
    hora = models.CharField(max_length=15)
    foto = models.URLField(max_length=200)
    evento= models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='actividades')

    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = "Actividad"
        verbose_name_plural = "Actividades"

class Organizador(AbstractUser):
    dni = models.CharField(max_length=9)
    foto_perfil= models.URLField(max_length=200)

    def __str__(self):
        return self.username
    class Meta:
        verbose_name = "Organizador"
        verbose_name_plural = "Organizadores"

class Inscripcion(models.Model):
    evento=models.ForeignKey(Evento,on_delete=models.CASCADE, related_name='evento')
    nombre = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = "Inscripcion"
        verbose_name_plural = "Inscripciones"