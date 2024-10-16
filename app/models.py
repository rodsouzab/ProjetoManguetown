from django.db import models
from django.db import models
from django.contrib.auth.models import User


from django.db import models
from django.contrib.auth.models import User

class Colaboradora(models.Model):
    nome = models.CharField(max_length=100,default='Nome Padrão')
    cpf = models.CharField(max_length=14)
    lugar_onde_mora = models.CharField(max_length=100, default='Não especificado')  # Adicionando um valor padrão
    renda = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Adicionando um valor padrão
    situacoes_vulnerabilidade = models.TextField(default='Não especificado')  # Adicionando um valor padrão
    quantos_filhos = models.IntegerField(default=0)  # Adicionando um valor padrão
    quantas_pessoas_moram = models.IntegerField(default=1)  # Adicionando um valor padrão
    habilidades = models.TextField(default='Não especificado')  # Adicionando um valor padrão
    usuario = models.OneToOneField(User, on_delete=models.CASCADE,default='Nome Padrão')

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
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_empresa