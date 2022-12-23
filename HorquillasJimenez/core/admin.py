from django.contrib import admin
from .models import *


##se crea las opciones para la manipulacion de los modelos a traves del sitio admin de django

admin.site.register(Maquina)
admin.site.register(Cliente)
admin.site.register(Operador)
admin.site.register(Inicio)
admin.site.register(Estado)
