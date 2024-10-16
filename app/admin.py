from django.contrib import admin

from .models import Colaboradora

admin.site.register(Colaboradora)

from .models import EmpresaParceira  # Importe o modelo EmpresaParceira

# Registre o modelo EmpresaParceira no admin
admin.site.register(EmpresaParceira)