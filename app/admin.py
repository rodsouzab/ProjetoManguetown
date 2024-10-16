from django.contrib import admin

from .models import Colaborador

admin.site.register(Colaborador)

from .models import EmpresaParceira  # Importe o modelo EmpresaParceira

# Registre o modelo EmpresaParceira no admin
admin.site.register(EmpresaParceira)