from django.db import models

# Create your models here.

class Colaborador(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    data_nascimento = models.DateField(null=True, blank=True)
    lugar_onde_mora = models.CharField(max_length=255)
    renda = models.DecimalField(max_digits=10, decimal_places=2)
    situacoes_de_vulnerabilidade = models.TextField(blank=True, null=True)
    quantos_filhos = models.PositiveIntegerField(default=0)
    quantas_pessoas_moram_com_voce = models.PositiveIntegerField(default=0)
    habilidades = models.TextField()

    def __str__(self):
        return self.nome
