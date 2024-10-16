from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Colaboradora, EmpresaParceira
from django.contrib import messages
from django.contrib.auth.decorators import login_required
def home(request):
    return render(request, 'home.html')

def sobre(request):
    return render(request, 'sobre.html')

def contato(request):
    return render(request, 'contato.html')

# View de login
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('manguetown:escolha_cadastro')
        else:
            # Adiciona uma mensagem de erro se a autenticação falhar
            messages.error(request, 'Usuário ou senha incorretos.')
    return render(request, 'login.html')

# View de registro de usuário
def registro_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Esse nome de usuário já está em uso.')
            return render(request, 'registro.html')  # Renderize o formulário novamente
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        return redirect('login')
    return render(request, 'registro.html')

# View para escolher tipo de cadastro
def escolha_cadastro_view(request):
    return render(request, 'escolha_cadastro.html')

# View de cadastro de colaboradora
@login_required
def cadastro_colaboradora_view(request):
    usuario = request.user

    if request.method == 'POST':
        # Verifica se o usuário já tem uma instância de Colaboradora
        if Colaboradora.objects.filter(usuario=usuario).exists():
            # Se já existe, retorna uma mensagem de erro em vez de redirecionar
            messages.error(request, "Você já está cadastrado como colaboradora.")
            return render(request, 'cadastro_colaboradora.html')  # Renderiza a mesma página com mensagem

        # Se não existe, cria a nova instância
        colaboradora = Colaboradora(
            nome=request.POST['nome'],
            cpf=request.POST['cpf'],
            lugar_onde_mora=request.POST['lugar_onde_mora'],
            renda=request.POST['renda'],
            situacoes_vulnerabilidade=request.POST['situacoes_vulnerabilidade'],
            quantos_filhos=request.POST['quantos_filhos'],
            quantas_pessoas_moram=request.POST['quantas_pessoas_moram'],
            habilidades=request.POST['habilidades'],
            usuario=usuario
        )

        try:
            colaboradora.save()  # Tente salvar a colaboradora
            messages.success(request, "Colaboradora cadastrada com sucesso!")  # Mensagem de sucesso
            return redirect('manguetown:escolha_cadastro')  # Redireciona para a página de sucesso

        except Exception as e:
            messages.error(request, f"Ocorreu um erro ao cadastrar: {str(e)}")  # Mensagem de erro

    return render(request, 'cadastro_colaboradora.html')  # Renderiza o template do for

# View de cadastro de empresa parceira
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import EmpresaParceira  # Supondo que o modelo EmpresaParceira já esteja importado

@login_required
def cadastro_empresa_view(request):
    usuario = request.user  # Obtém o usuário logado

    if request.method == 'POST':
        # Verifica se o usuário já possui um cadastro de empresa
        if EmpresaParceira.objects.filter(usuario=usuario).exists():
            messages.error(request, "Você já está cadastrado como empresa parceira.")
            return render(request, 'cadastro_empresa.html')

        # Criação de uma nova instância de EmpresaParceira
        empresa = EmpresaParceira(
            nome_responsavel=request.POST.get('nome_responsavel'),
            nome_empresa=request.POST.get('nome_empresa'),
            captacao_local=request.POST.get('captacao_local'),
            disponibilidade_residuo=request.POST.get('disponibilidade_residuo'),
            porte_fabrico=request.POST.get('porte_fabrico'),
            tipo_residuo=request.POST.get('tipo_residuo'),
            condicao_residuo=request.POST.get('condicao_residuo'),
            usuario=usuario  # Associando a empresa ao usuário logado
        )

        try:
            empresa.save()  # Tenta salvar a nova empresa
            messages.success(request, "Empresa cadastrada com sucesso!")
            return redirect('manguetown:escolha_cadastro')
        except Exception as e:
            messages.error(request, f"Erro ao cadastrar a empresa: {e}")

    return render(request, 'cadastro_empresa.html')