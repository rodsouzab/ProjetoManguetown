# Generated by Django 5.1.2 on 2024-10-16 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_empresaparceira_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresaparceira',
            name='captacao_local',
            field=models.CharField(default='Local não especificado', max_length=100),
        ),
        migrations.AlterField(
            model_name='empresaparceira',
            name='condicao_residuo',
            field=models.TextField(default='Não especificado'),
        ),
    ]
