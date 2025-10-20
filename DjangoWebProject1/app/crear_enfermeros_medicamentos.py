import os
import django
import json
from datetime import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoWebProject1.settings')
django.setup()

from app.models import Enfermero, Medicamento

def cargar_enfermeros_desde_json(ruta_archivo):
    with open(ruta_archivo, 'r', encoding='utf-8') as f:
        datos = json.load(f)
    
    for item in datos:
        fecha_inicio = datetime.strptime(item['inicio_contrato'], '%Y-%m-%d').date()
        Enfermero.objects.create(
            id=item['id'],
            nombre=item['nombre'],
            apellido=item['apellido'],
            clientes=None,  # O asigna si tienes relaciones
            salario=item['salario'],
            inicio_contrato=fecha_inicio,
            numero_seguridad_social=item['numero_seguridad_social']
        )
    print("Enfermeros cargados correctamente.")

def cargar_medicamentos_desde_json(ruta_archivo):
    with open(ruta_archivo, 'r', encoding='utf-8') as f:
        datos = json.load(f)
        
    for item in datos:
        fecha_caducidad = datetime.strptime(item['CADUCIDAD'], '%Y-%m-%d').date()
        Medicamento.objects.create(
            id=item['ID'],
            nombre=item['NOMBRE'],
            dosis=item['DOSIS'],
            marca=item['MARCA'],
            caducidad=fecha_caducidad,
            stock=item['STOCK']
        )
    print("Medicamentos cargados correctamente.")

if __name__ == "__main__":
    cargar_enfermeros_desde_json(r'app\Json\enfermeros.json')
    cargar_medicamentos_desde_json(r'app\Json\medicamentos.json')
