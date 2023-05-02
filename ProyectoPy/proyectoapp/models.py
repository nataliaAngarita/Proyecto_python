from django.db import models

# Create your models here.

class Producto(models.Model):
    categoria = models.CharField(max_length=40)
    nombre = models.CharField(max_length=40)
    precio = models.IntegerField()

class Cliente(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)

class Vendedor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    categoria = models.CharField(max_length=30)