from django.db import models

# Create your models here.



from django.db import models
from django.contrib.auth.models import User

class Colaborador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,default=None)
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14, unique=True)
    data_nascimento = models.DateField(blank=True, null=True)
    lugar_onde_mora = models.CharField(max_length=255)
    renda = models.DecimalField(max_digits=10, decimal_places=2)
    situacoes_de_vulnerabilidade = models.TextField(blank=True, null=True)
    quantos_filhos = models.PositiveIntegerField(default=0)
    quantas_pessoas_moram_com_voce = models.PositiveIntegerField(default=0)
    habilidades = models.TextField(null=True)
    email = models.EmailField(default='nao_informado@example.com')  # Novo campo
    telefone = models.CharField(max_length=15,default='0000000000')  # Novo campo

    def __str__(self):
        return self.nome

class EmpresaParceira(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,default=None)
    nome = models.CharField(max_length=255)
    lugar_mora = models.CharField(max_length=255)
    local_captacao = models.CharField(max_length=255)
    disponibilidade_residuo = models.TextField(null=True)
    descricao = models.TextField(null=True)
    fabricacao_porte = models.CharField(max_length=50)
    residuo_tipo = models.CharField(max_length=50)
    telefone = models.CharField(max_length=15,default='0000000000')
    email = models.EmailField(default='nao_informado@example.com')
    condicao_residuo = models.TextField(null=True)