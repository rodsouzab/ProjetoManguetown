from django.db import models
from django.contrib.auth.models import User

class Colaborador(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    data_nascimento = models.DateField(null=True, blank=True)
    lugar_onde_mora = models.CharField(max_length=255)
    renda = models.DecimalField(max_digits=10, decimal_places=2)
    situacoes_de_vulnerabilidade = models.TextField(blank=True, null=True, default='Não especificado')
    quantos_filhos = models.PositiveIntegerField(default=0)
    quantas_pessoas_moram_com_voce = models.PositiveIntegerField(default=0)
    habilidades = models.TextField(default='Não especificado')
    
    # O usuário é diferente do colaborador ?
    # usuario = models.OneToOneField(User, on_delete=models.CASCADE,default='Nome Padrão')


    def __str__(self):
        return self.nome


class EmpresaParceira(models.Model):
    nome_responsavel = models.CharField(max_length=100, default='Nome Padrão')
    nome_empresa = models.CharField(max_length=100, default='Nome Padrão')
    captacao_local = models.CharField(max_length=100, default='Local não especificado')
    disponibilidade_residuo = models.CharField(max_length=100, default='Não especificado')
    porte_fabrico = models.CharField(
        max_length=50,
        choices=[('pequeno', 'Pequeno'), ('medio', 'Médio'), ('grande', 'Grande')],
        default='pequeno'
    )
    tipo_residuo = models.CharField(max_length=100, default='Não especificado')
    condicao_residuo = models.TextField(default='Não especificado')
    
    # O campo `usuario` não deve ter valor padrão; o usuário logado será associado aqui
    #usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_empresa
