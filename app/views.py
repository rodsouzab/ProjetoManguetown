from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Colaborador, EmpresaParceira, Boneca, Doador, Colaborador
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
import re


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
            return redirect('manguetown:dashboard')
        else:
            messages.error(request, 'Usuário ou senha incorretos.')
    return render(request, 'login.html')

# View de registro de usuário
def registro_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST.get('email')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Esse nome de usuário já está em uso.')
            return render(request, 'registro.html')  # Renderize o formulário novamente
        user = User.objects.create_user(username=username, password=password, email=email)
        if not email:
            messages.error(request, 'O campo de e-mail é obrigatório.')
            return render(request, 'registro.html')
        user.save()
        return render(request, 'login.html')
    return render(request, 'registro.html')

# View para escolher a página de gestão
@login_required
def dashboard_view(request):
    return render(request, 'dashboard.html')

# View da página de gestão de colaboradores
def gestao_colaboradores_view(request):
    colaboradores = Colaborador.objects.all()
    return render(request, 'gestao_colaboradores.html', {'colaboradores': colaboradores})

# View da página de gestão de colaboradores
def gestao_empresas_view(request):
    empresas = EmpresaParceira.objects.all()
    return render(request, 'gestao_empresas.html', {'empresas': empresas})

# View para o cadastro de colaborador
def cadastrar_colaborador_view(request):
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
        
        # Verifica se o CPF contém apenas números
        if not re.match(r'^\d+$', cpf):
            messages.error(request, 'O CPF deve conter apenas números.')
            return redirect('manguetown:cadastrar_colaborador')
        
        # Verifica se o CPF já existe antes de tentar salvar
        if Colaborador.objects.filter(cpf=cpf).exists():
            messages.error(request, 'O CPF já está cadastrado. Por favor, insira um CPF diferente.')
            return redirect('manguetown:cadastrar_colaborador')  # Redireciona de volta ao formulário

        try:
            Colaborador.objects.create(
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
            # Não mostrar mensagem de sucesso aqui
            return redirect('manguetown:gestao_colaboradores')  # Redireciona para a página de Gestão de Colaboradores

        except IntegrityError:
            messages.error(request, 'Erro ao cadastrar colaborador. Por favor, tente novamente.')
            return redirect('manguetown:cadastrar_colaborador')  # Redireciona de volta ao formulário

    return render(request, 'cadastrar_colaborador.html')

# View para escolher tipo de cadastro
# def escolha_cadastro_view(request):
#     return render(request, 'escolha_cadastro.html')

# View de cadastro de colaboradora
# def cadastro_colaboradora_view(request):
#     usuario = request.user

#     if request.method == 'POST':
#         # Verifica se o usuário já tem uma instância de Colaboradora
#         if Colaboradora.objects.filter(usuario=usuario).exists():
#             # Se já existe, retorna uma mensagem de erro em vez de redirecionar
#             messages.error(request, "Você já está cadastrado como colaboradora.")
#             return render(request, 'cadastro_colaboradora.html')  # Renderiza a mesma página com mensagem

#         # Se não existe, cria a nova instância
#         colaboradora = Colaboradora(
#             nome=request.POST['nome'],
#             cpf=request.POST['cpf'],
#             lugar_onde_mora=request.POST['lugar_onde_mora'],
#             renda=request.POST['renda'],
#             situacoes_vulnerabilidade=request.POST['situacoes_vulnerabilidade'],
#             quantos_filhos=request.POST['quantos_filhos'],
#             quantas_pessoas_moram=request.POST['quantas_pessoas_moram'],
#             habilidades=request.POST['habilidades'],
#             usuario=usuario
#         )

#         try:
#             colaboradora.save()  # Tente salvar a colaboradora
#             messages.success(request, "Colaboradora cadastrada com sucesso!")  # Mensagem de sucesso
#             return redirect('manguetown:escolha_cadastro')  # Redireciona para a página de sucesso

#         except Exception as e:
#             messages.error(request, f"Ocorreu um erro ao cadastrar: {str(e)}")  # Mensagem de erro

#     return render(request, 'cadastro_colaboradora.html')  # Renderiza o template do for

# View de cadastro de empresa parceira
@login_required
def cadastro_empresa_view(request):
    if request.method == 'POST':
        nome_empresa = request.POST.get('nome_empresa')

        # Verifica se o usuário já possui um cadastro de empresa
        if EmpresaParceira.objects.filter(nome_empresa=nome_empresa).exists():
            messages.error(request, "Você já está cadastrado como empresa parceira.")
            return render(request, 'cadastro_empresa.html')

        # Criação de uma nova instância de EmpresaParceira
        empresa = EmpresaParceira(
            nome_responsavel=request.POST.get('nome_responsavel'),
            nome_empresa=nome_empresa,
            captacao_local=request.POST.get('captacao_local'),
            disponibilidade_residuo=request.POST.get('disponibilidade_residuo'),
            porte_fabrico=request.POST.get('porte_fabrico'),
            tipo_residuo=request.POST.get('tipo_residuo'),
            condicao_residuo=request.POST.get('condicao_residuo'),
            # Removido o campo 'usuario' da instância
        )

        try:
            empresa.save()  # Tenta salvar a nova empresa
            return redirect('manguetown:gestao_empresas')
        except Exception as e:
            messages.error(request, f"Erro ao cadastrar a empresa: {e}")

    return render(request, 'cadastro_empresa.html')

@login_required
def editar_empresa_view(request, empresa_id=None):
    # Busca a empresa existente usando o ID, se ele for fornecido
    empresa = None
    if empresa_id:
        try:
            empresa = EmpresaParceira.objects.get(id=empresa_id)
        except EmpresaParceira.DoesNotExist:
            messages.error(request, "Empresa não encontrada.")
            return redirect('manguetown:gestao_empresas')

    if request.method == 'POST':
        nome_empresa = request.POST.get('nome_empresa')

        # Verifica se o usuário está tentando cadastrar uma empresa com um nome já existente
        if not empresa and EmpresaParceira.objects.filter(nome_empresa=nome_empresa).exists():
            messages.error(request, "Uma empresa com esse nome já existe.")
            return render(request, 'editar_empresa.html', {'empresa': empresa})

        # Atualiza os dados da empresa existente ou cria uma nova instância
        if not empresa:
            empresa = EmpresaParceira()

        empresa.nome_responsavel = request.POST.get('nome_responsavel')
        empresa.nome_empresa = nome_empresa
        empresa.captacao_local = request.POST.get('captacao_local')
        empresa.disponibilidade_residuo = request.POST.get('disponibilidade_residuo')
        empresa.porte_fabrico = request.POST.get('porte_fabrico')
        empresa.tipo_residuo = request.POST.get('tipo_residuo')
        empresa.condicao_residuo = request.POST.get('condicao_residuo')

        try:
            empresa.save()  # Tenta salvar a empresa editada
            messages.success(request, "Empresa atualizada com sucesso!")
            return redirect('manguetown:gestao_empresas')
        except Exception as e:
            messages.error(request, f"Erro ao atualizar a empresa: {e}")

    # Carrega os dados da empresa existente no formulário
    context = {'empresa': empresa}
    return render(request, 'editar_empresa.html', context)

@login_required
def gestao_colaboradores_view(request):
    if request.method == 'POST':
        colaborador_id = request.POST.get('colaborador_id')
        if colaborador_id:    
            try:
                colaborador = get_object_or_404(Colaborador, id=colaborador_id)
                colaborador.delete()
                messages.success(request, "Colaborador excluído com sucesso!")
            except Exception as e:
                messages.error(request, f"Erro ao excluir colaborador: {e}")
            
            return redirect('manguetown:gestao_colaboradores')

    colaboradores = Colaborador.objects.all()
    return render(request, 'gestao_colaboradores.html', {'colaboradores': colaboradores})

@login_required
def gestao_doadores_view(request):
    if request.method == 'POST':
        doador_id = request.POST.get('doador_id')
        if doador_id:
            try:
                doador = get_object_or_404(Doador, id=doador_id)
                doador.delete()
                messages.success(request, "Doador excluído com sucesso!")
            except Exception as e:
                messages.error(request, f"Erro ao excluir doador: {e}")

            return redirect('manguetown:gestao_doadores')

    doadores = Doador.objects.all()
    return render(request, 'gestao_doadores.html', {'doadores': doadores})

@login_required
def gestao_empresas_view(request):
    if request.method == 'POST':
        empresa_id = request.POST.get('empresa_id')
        try:
            empresa = get_object_or_404(EmpresaParceira, id=empresa_id)
            empresa.delete()
            messages.success(request, "Empresa excluída com sucesso!")
        except Exception as e:
            messages.error(request, f"Erro ao excluir empresa: {e}")

        return redirect('manguetown:gestao_empresas')

    empresas = EmpresaParceira.objects.all()
    return render(request, 'gestao_empresas.html', {'empresas': empresas})

@login_required
def cadastrar_boneca_view(request):
    if request.method == 'POST':
        nome = request.POST.get('nome_boneca')
        quantidade = request.POST.get('quantidade')
        nivel_dificuldade = request.POST.get('nivel_dificuldade')
        colaborador_id = request.POST.get('colaborador_id') 

        # Verifica se o colaborador existe
        try:
            colaborador = Colaborador.objects.get(id=colaborador_id)
        except Colaborador.DoesNotExist:
            messages.error(request, "Colaborador não encontrado.")
            return redirect('manguetown:cadastrar_boneca')

        # Criação da nova boneca
        boneca = Boneca(
            colaborador=colaborador,
            nome=nome,
            quantidade=quantidade,
            nivel_dificuldade=nivel_dificuldade
        )

        try:
            boneca.save()  # Tenta salvar a nova boneca
            return redirect('manguetown:gestao_bonecas')  # Redireciona para a página de gestão de bonecas
        except Exception as e:
            messages.error(request, f"Erro ao cadastrar a boneca: {e}")

    # Obtém todos os colaboradores cadastrados para o dropdown
    colaboradores = Colaborador.objects.all()
    return render(request, 'cadastrar_boneca.html', {'colaboradores': colaboradores})

@login_required
def gestao_bonecas_view(request):
    if request.method == 'POST':
        boneca_id = request.POST.get('boneca_id')
        try:
            boneca = Boneca.objects.get(id=boneca_id)
            boneca.delete()
            messages.success(request, "Boneca excluída com sucesso!")
        except Boneca.DoesNotExist:
            messages.error(request, "Boneca não encontrada.")
        except Exception as e:
            messages.error(request, f"Erro ao excluir a boneca: {e}")

    bonecas = Boneca.objects.all()
    return render(request, 'gestao_bonecas.html', {'bonecas': bonecas})



@login_required
def cadastrar_doador_view(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        data_nascimento = request.POST.get('data_nascimento')
        lugar_onde_mora = request.POST.get('lugar_onde_mora')
        individual = request.POST.get('individual') == 'True'  # Convertendo para booleano
        tipo_doador = request.POST.get('tipo_doador')
        data_disponibilidade = request.POST.get('data_disponibilidade')
        local_captacao = request.POST.get('local_captacao')
        condicao_residuo = request.POST.get('condicao_residuo')
        tipo_residuo = request.POST.get('tipo_residuo')

        # Verifica se o CPF já existe
        if Doador.objects.filter(cpf=cpf).exists():
            messages.error(request, 'O CPF já está cadastrado. Por favor, insira um CPF diferente.')
            return render(request, 'cadastrar_doador.html')  # Retorna ao formulário com mensagem

        # Se o tipo doador for Financiador, não preenche os outros campos
        if tipo_doador == 'Financiador':
            data_disponibilidade = None
            local_captacao = None
            condicao_residuo = None
            tipo_residuo = None

        doador = Doador(
            nome=nome,
            cpf=cpf,
            data_nascimento=data_nascimento,
            lugar_onde_mora=lugar_onde_mora,
            individual=individual,
            tipo_doador=tipo_doador,
            data_disponibilidade=data_disponibilidade,
            local_captacao=local_captacao,
            condicao_residuo=condicao_residuo,
            tipo_residuo=tipo_residuo
        )

        try:
            doador.save()  # Tenta salvar a nova doador
            messages.success(request, 'Doador cadastrado com sucesso!')
            return redirect('manguetown:gestao_doadores')  # Redireciona para a página de gestão de doadores
        except Exception:
            messages.error(request, 'Erro ao cadastrar doador. Por favor, tente novamente.')
            return render(request, 'cadastrar_doador.html')  # Retorna ao formulário com mensagem

    return render(request, 'cadastrar_doador.html')

@login_required
def editar_doador_view(request, doador_id):
    doador = get_object_or_404(Doador, id=doador_id)

    if request.method == 'POST':
        # Captura os dados do formulário
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        data_nascimento = request.POST.get('data_nascimento')
        lugar_onde_mora = request.POST.get('lugar_onde_mora')
        individual = request.POST.get('individual') == 'True'
        tipo_doador = request.POST.get('tipo_doador')
        data_disponibilidade = request.POST.get('data_disponibilidade')
        local_captacao = request.POST.get('local_captacao')
        condicao_residuo = request.POST.get('condicao_residuo')
        tipo_residuo = request.POST.get('tipo_residuo')

        # Verifica se o CPF já existe e se não é o CPF do próprio doador
        if Doador.objects.filter(cpf=cpf).exclude(id=doador.id).exists():
            messages.error(request, 'O CPF já está cadastrado. Por favor, insira um CPF diferente.')
            return render(request, 'editar_doador.html', {'doador': doador})

        # Atualiza os dados do doador
        doador.nome = nome
        doador.cpf = cpf
        doador.data_nascimento = data_nascimento
        doador.lugar_onde_mora = lugar_onde_mora
        doador.individual = individual
        doador.tipo_doador = tipo_doador
        doador.data_disponibilidade = data_disponibilidade
        doador.local_captacao = local_captacao
        doador.condicao_residuo = condicao_residuo
        doador.tipo_residuo = tipo_residuo

        try:
            doador.save()  # Tenta salvar as alterações
            messages.success(request, 'Doador editado com sucesso!')
            return redirect('manguetown:gestao_doadores')  # Redireciona para a página de gestão de doadores
        except Exception:
            messages.error(request, 'Erro ao atualizar doador. Por favor, tente novamente.')
            return render(request, 'editar_doador.html', {'doador': doador})

    return render(request, 'editar_doador.html', {'doador': doador})



@login_required
def editar_colaborador_view(request, id):
    colaborador = get_object_or_404(Colaborador, id=id)

    if request.method == 'POST':
        # Obtém os dados do formulário
        colaborador.nome = request.POST['nome']
        cpf = request.POST['cpf']
        
        # Verifica se o CPF contém apenas números
        if not re.match(r'^\d+$', cpf):
            messages.error(request, 'O CPF deve conter apenas números.')
            return render(request, 'editar_colaborador.html', {'colaborador': colaborador})
        
        # Verifica se o CPF já existe antes de tentar salvar, ignorando o colaborador atual
        if Colaborador.objects.exclude(id=id).filter(cpf=cpf).exists():
            messages.error(request, 'O CPF já está cadastrado. Por favor, insira um CPF diferente.')
            return render(request, 'editar_colaborador.html', {'colaborador': colaborador})
        
        colaborador.cpf = cpf
        colaborador.data_nascimento = request.POST['data_nascimento']
        colaborador.lugar_onde_mora = request.POST['lugar_onde_mora']
        
        renda_str = request.POST['renda']
        # Normaliza a string de renda para um formato aceito pelo float
        renda_str = renda_str.replace(',', '.')  # Substitui vírgulas por pontos

        try:
            colaborador.renda = float(renda_str)  # Converter renda para float
        except ValueError:
            messages.error(request, 'Por favor, insira um valor de renda válido.')
            return render(request, 'editar_colaborador.html', {'colaborador': colaborador})

        colaborador.situacoes_de_vulnerabilidade = request.POST['situacoes_de_vulnerabilidade']
        colaborador.quantos_filhos = request.POST['quantos_filhos']
        colaborador.quantas_pessoas_moram_com_voce = request.POST['quantas_pessoas_moram_com_voce']
        colaborador.habilidades = request.POST['habilidades']

        # Salva as alterações no colaborador
        colaborador.save()
        messages.success(request, "Colaborador editado com sucesso!")
        return redirect('manguetown:gestao_colaboradores')

    return render(request, 'editar_colaborador.html', {'colaborador': colaborador})



from django.shortcuts import render
from django.db.models import Sum
from .models import Colaborador

def dashboard_view(request):
    # Buscar todos os colaboradores com a soma da quantidade de bonecas que cada um tem
    colaboradores = Colaborador.objects.annotate(total_bonecas=Sum('boneca__quantidade'))

    dados_bonecas = []
    dados_desempenho = []

    for colaborador in colaboradores:
        # Dados para o gráfico de bonecas
        dados_bonecas.append({
            'nome': colaborador.nome,
            'quantidade': colaborador.total_bonecas or 0  # Se não houver bonecas, coloca 0
        })
        
        # Calcular os pontos do colaborador com base no nível de dificuldade das bonecas
        total_pontos = 0
        for boneca in colaborador.boneca_set.all():
            if boneca.nivel_dificuldade == '1':
                total_pontos += boneca.quantidade * 1  # Nível 1: 1 ponto por boneca
            elif boneca.nivel_dificuldade == '2':
                total_pontos += boneca.quantidade * 1.5  # Nível 2: 1.5 pontos por boneca
            elif boneca.nivel_dificuldade == '3':
                total_pontos += boneca.quantidade * 2  # Nível 3: 2 pontos por boneca
            # Adicione mais condições conforme os níveis de dificuldade

        # Dados para o gráfico de desempenho
        dados_desempenho.append({
            'nome': colaborador.nome,
            'pontos': total_pontos
        })
    
    # Passando os dados para o template
    return render(request, 'dashboard.html', {
        'dados_bonecas': dados_bonecas,
        'dados_desempenho': dados_desempenho
    })
