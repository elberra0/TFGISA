"""
Definition of models.
"""

from django.db import models

class Medicamento(models.Model):
    nombre = models.CharField(max_length=100)
    dosis = models.CharField(max_length=50)
    marca = models.CharField(max_length=100)
    caducidad = models.DateField()
    stock = models.PositiveIntegerField()

class Enfermero(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    clientes = models.ManyToManyField('Cliente', blank=True)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    inicio_contrato = models.DateField()
    numero_seguridad_social = models.CharField(max_length=20, unique=True)


class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=100)
    edad = models.IntegerField()
    fecha_ingreso = models.DateField()
    medicamentos = models.ForeignKey(Medicamento, null=True, blank=True, on_delete=models.SET_NULL)
    enfermero_asignado = models.ForeignKey(
    Enfermero,
    null=True,
    blank=True,
    on_delete=models.SET_NULL,
    related_name='clientes_asignados'
)

