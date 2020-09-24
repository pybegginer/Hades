from config.wsgi import *
from core.erp.models import Type

#Crear algunas consultas
# TypeList = ['Ingeniero', 'Analista', 'Senior', 'Backend Developer', 'Frontend']
#
# for i in TypeList:
#     newType = Type()
#     newType.name=i
#     newType.save()
#     print(f'Se han creado el tipo {i}')
#
#----Listar filtrado
k = Type.objects.filter(name__icontains='eN')


