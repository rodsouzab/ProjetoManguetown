
from django.contrib import admin
from django.urls import path
from app import views
from app.views import login_view  
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

app_name = "manguetown"
urlpatterns = [
    path('', views.home, name='home'),
    path('sobre/', views.sobre, name='sobre'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('contato/', views.contato, name='contato'),
    path('registro/', views.registro_view, name='registro'),
    # path('escolha-cadastro/', views.escolha_cadastro_view, name='escolha_cadastro'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('gestao_colaboradores/', views.gestao_colaboradores_view, name='gestao_colaboradores'),
    path('cadastrar_colaborador/', views.cadastrar_colaborador_view, name='cadastrar_colaborador'),
    path('cadastro-empresa/', views.cadastro_empresa_view, name='cadastro_empresa'),
    path('gestao_empresas/', views.gestao_empresas_view, name='gestao_empresas'),
]