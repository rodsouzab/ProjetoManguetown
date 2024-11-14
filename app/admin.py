from django.contrib import admin
from .models import Colaborador, Boneca, EmpresaParceira, Doador
# admin.site.register(Colaborador)

# Registre o modelo EmpresaParceira no admin
admin.site.register(EmpresaParceira)

@admin.register(Boneca)
class BonecaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nivel_dificuldade', 'colaborador')  # Campos a serem exibidos na lista
    search_fields = ('nome',)  # Permite busca pelo nome da boneca
    
@admin.register(Colaborador)
class ColaboradorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'data_nascimento')
    
admin.site.register(Doador)