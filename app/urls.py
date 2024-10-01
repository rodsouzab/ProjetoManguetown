
from django.contrib import admin
from django.urls import path
from app import views
from app.views import login_view  
from django.views.generic import TemplateView
app_name = "manguetown"
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('sobre/', views.sobre, name='sobre'),
    path('contato/', views.contato, name='contato'),
    path('cadastrar/', TemplateView.as_view(template_name='cadastro.html'), name='cadastrar'),
    path('colaborador/cadastrar/', views.cadastrar_colaborador, name='colaborador'),
    path('empresa/cadastrar/', views.cadastrar_empresa, name='empresa'),
]