from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from .models import Colaborador


# Create your views here.

def home(request):
    return render(request, 'home.html')

def sobre(request):
    return render(request, 'sobre.html')

def contato(request):
    return render(request, 'contato.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def gestao_colaboradores(request):
    return render(request, 'gestao_colaboradores.html')

def cadastrar_colaborador(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        cpf = request.POST['cpf']
        data_nascimento = request.POST['data_nascimento']
        lugar_onde_mora = request.POST['lugar_onde_mora']
        renda = request.POST['renda']
        situacoes_de_vulnerabilidade = request.POST['situacoes_de_vulnerabilidade']
        quantos_filhos = request.POST['quantos_filhos']
        quantas_pessoas_moram_com_voce = request.POST['quantas_pessoas_moram_com_voce']
        habilidades = request.POST['habilidades']
        
        novo_colaborador = Colaborador.objects.create(
            nome=nome,
            cpf=cpf,
            data_nascimento=data_nascimento,
            lugar_onde_mora=lugar_onde_mora,
            renda=renda,
            situacoes_de_vulnerabilidade=situacoes_de_vulnerabilidade,
            quantos_filhos=quantos_filhos,
            quantas_pessoas_moram_com_voce=quantas_pessoas_moram_com_voce,
            habilidades=habilidades,
        )
        
        return redirect('manguetown:gestao_colaboradores')
    
    return render(request, 'cadastrar_colaborador.html')

def gestao_colaboradores(request):
    colaboradores = Colaborador.objects.all()
    return render(request, 'gestao_colaboradores.html', {'colaboradores': colaboradores})


class LoginView(auth_views.LoginView):
    template_name = 'login.html'