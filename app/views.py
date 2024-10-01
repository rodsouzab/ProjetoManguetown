from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from .models import EmpresaParceira
from .models import Colaborador
# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Colaborador, EmpresaParceira
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Colaborador, EmpresaParceira
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def sobre(request):
    return render(request, 'sobre.html')

def contato(request):
    return render(request, 'contato.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('home')
    return render(request, 'login.html')

# views.py

# View para cadastro de Colaborador
from django.shortcuts import render, redirect
from .models import Colaborador, EmpresaParceira
from django.http import HttpResponse

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('home')
        else:
            messages.error(request, "Nome de usuário ou senha inválidos.")
    return render(request, 'login.html')

# View para cadastro de Colaborador
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Colaborador
from django.contrib.auth.models import User

def cadastrar_colaborador(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirmar_senha = request.POST.get('confirmar_senha')
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        lugar_mora = request.POST.get('lugar_mora')
        renda = request.POST.get('renda')
        situacoes_vulnerabilidade = request.POST.get('situacoes_vulnerabilidade')
        quantos_filhos = request.POST.get('filhos')
        quantas_pessoas_moram_com_voce = request.POST.get('pessoas_moram_com_voce')
        habilidades = request.POST.get('habilidades')
        email = request.POST.get('email')  # Novo campo
        telefone = request.POST.get('telefone')  # Novo campo

        # Verifica se as senhas coincidem
        if password != confirmar_senha:
            messages.error(request, "As senhas não coincidem.")
            return render(request, 'colaborador.html')

        # Verificando se o nome de usuário já existe
        if User.objects.filter(username=username).exists():
            messages.error(request, "Esse nome de usuário já está em uso.")
            return render(request, 'colaborador.html')

        # Criar o usuário
        user = User.objects.create_user(username=username, password=password)

        # Criar o colaborador associado ao usuário
        Colaborador.objects.create(
            user=user,
            nome=nome,
            cpf=cpf,
            lugar_onde_mora=lugar_mora,
            renda=renda,
            situacoes_vulnerabilidade=situacoes_vulnerabilidade,
            quantos_filhos=quantos_filhos,
            quantas_pessoas_moram_com_voce=quantas_pessoas_moram_com_voce,
            habilidades=habilidades,
            email=email,  # Novo campo
            telefone=telefone  # Novo campo
        )
        
        messages.success(request, "Colaborador cadastrado com sucesso!")
        return redirect('login')

    return render(request, 'colaborador.html')  # Renderiza o template de cadastro



# View para cadastro de Empresa Parceira
def cadastrar_empresa(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        nome = request.POST.get('nome')
        lugar_mora = request.POST.get('lugar_mora')
        local_captacao = request.POST.get('local_captacao')
        disponibilidade_residuo = request.POST.get('disponibilidade_residuo')
        descricao = request.POST.get('descricao')
        fabricacao_porte = request.POST.get('fabricacao_porte')
        residuo_tipo = request.POST.get('residuo_tipo')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        condicao_residuo = request.POST.get('condicao_residuo')

        # Verificando se o nome de usuário já existe
        if User.objects.filter(username=username).exists():
            messages.error(request, "Esse nome de usuário já está em uso.")
            return render(request, 'empresa.html')

        # Criar o usuário
        user = User.objects.create_user(username=username, password=password)
        if user:
            messages.success(request, "Usuário criado com sucesso!")
        else:
            messages.error(request, "Erro ao criar o usuário.")
        # Criar a empresa parceira associada ao usuário
        EmpresaParceira.objects.create(
            user=user,
            nome=nome,
            lugar_mora=lugar_mora,
            local_captacao=local_captacao,
            disponibilidade_residuo=disponibilidade_residuo,
            descricao=descricao,
            fabricacao_porte=fabricacao_porte,
            residuo_tipo=residuo_tipo,
            telefone=telefone,
            email=email,
            condicao_residuo=condicao_residuo
        )
        
        messages.success(request, "Empresa cadastrada com sucesso!")
        return redirect('login')

    return render(request, 'empresa.html')

