
from django.contrib import admin
from django.urls import path
from app import views
from app.views import LoginView

app_name = "manguetown"
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('sobre/', views.sobre, name='sobre'),
    path('contato/', views.contato, name='contato'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('gestao_colaboradoras/', views.gestao_colaboradoras, name='gestao_colaboradoras'),
]
