"""
Definition of models.
"""

from django.db import models

# Create your models here.

class Medicamento(models.Model):
    nombre = models.CharField(max_length=100)

class Enfermero(models.Model):
    nombre = models.CharField(max_length=100)

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=100)
    edad = models.IntegerField()
    fecha_ingreso = models.DateField()
    medicamentos = models.ForeignKey(Medicamento, null=True, blank=True, on_delete=models.SET_NULL)
    enfermero_asignado = models.ForeignKey(Enfermero, null=True, blank=True, on_delete=models.SET_NULL)
