import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoWebProject1.settings')
django.setup()

# Ahora puedes importar los modelos
from app.models import Cliente

import json
from datetime import datetime

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
    print("Datos cargados correctamente.")

# Si quieres ejecutar directamente cuando cargas el script:
if __name__ == "__main__":
    cargar_clientes_desde_json(r'app\Json\ancianos.json')
