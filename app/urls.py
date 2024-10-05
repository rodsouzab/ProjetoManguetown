
from django.contrib import admin
from django.urls import path
from app import views
from app.views import login_view  
from django.views.generic import TemplateView
app_name = "manguetown"
urlpatterns = [
    path('', views.home, name='home'),
    path('sobre/', views.sobre, name='sobre'),
    path('login/', views.login_view, name='login'),
    path('contato/', views.contato, name='contato'),
    path('registro/', views.registro_view, name='registro'),
    # path('escolha-cadastro/', views.escolha_cadastro_view, name='escolha_cadastro'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('gestao_colaboradores/', views.gestao_colaboradores_view, name='gestao_colaboradores'),
    path('cadastrar_colaborador/', views.cadastrar_colaborador_view, name='cadastrar_colaborador'),
    path('cadastro-empresa/', views.cadastro_empresa_view, name='cadastro_empresa'),
]