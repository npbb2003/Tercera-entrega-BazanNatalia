from django.db import models

# Create your models here.


class CopiaImpresa(models.Model):
    superficie = models.CharField(max_length=40)
    tamanio = models.IntegerField()
    precio = models.IntegerField()


class Fotolibro(models.Model):
    tamanio = models.IntegerField()
    cant_hojas = models.IntegerField()
    precio = models.IntegerField()


class SesionFotografica(models.Model):
    nombre = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=100)
    activo = models.BooleanField(default=False)
    precio = models.IntegerField()


class SesionDeFoto(models.Model):
    nombre = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=100)
    activo = models.BooleanField(default=False)
    precio = models.IntegerField()
