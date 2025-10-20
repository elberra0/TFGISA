import os
import django
import json
from datetime import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoWebProject1.settings')
django.setup()

from app.models import Cliente, Medicamento, Enfermero

def cargar_medicamentos_desde_json(ruta_archivo):
    with open(ruta_archivo, 'r', encoding='utf-8') as f:
        datos = json.load(f)
    for item in datos:
        fecha_cad = datetime.strptime(item['caducidad'], '%Y-%m-%d').date()
        Medicamento.objects.create(
            id=item['id'],
            nombre=item['nombre'],
            dosis=item['dosis'],
            marca=item['marca'],
            caducidad=fecha_cad,
            stock=item['stock']
        )
    print("Medicamentos cargados correctamente.")

def cargar_enfermeros_desde_json(ruta_archivo):
    with open(ruta_archivo, 'r', encoding='utf-8') as f:
        datos = json.load(f)
    for item in datos:
        fecha_inicio = datetime.strptime(item['inicio_contrato'], '%Y-%m-%d').date()
        Enfermero.objects.create(
            id=item['id'],
            nombre=item['nombre'],
            apellido=item['apellido'],
            salario=item['salario'],
            inicio_contrato=fecha_inicio,
            numero_seguridad_social=item['numero_seguridad_social']
        )
    print("Enfermeros cargados correctamente.")

def cargar_clientes_desde_json(ruta_archivo):
    with open(ruta_archivo, 'r', encoding='utf-8') as f:
        datos = json.load(f)
    for item in datos:
        fecha = datetime.strptime(item['fecha_ingreso'], '%Y-%m-%d').date()
        Cliente.objects.create(
            id=item['id'],
            nombre=item['nombre'],
            apellidos=item['apellidos'],
            edad=item['edad'],
            fecha_ingreso=fecha,
            medicamentos=None,
            enfermero_asignado=None
        )
    print("Clientes cargados correctamente.")

if __name__ == "__main__":
    cargar_medicamentos_desde_json(r'app\Json\medicamentos.json')
    cargar_enfermeros_desde_json(r'app\Json\enfermeros.json')
    cargar_clientes_desde_json(r'app\Json\ancianos.json')

