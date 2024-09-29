from django.shortcuts import render
from django.contrib.auth import views as auth_views

# Create your views here.

def home(request):
    return render(request, 'home.html')

def sobre(request):
    return render(request, 'sobre.html')

def contato(request):
    return render(request, 'contato.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def gestao_colaboradoras(request):
    return render(request, 'gestao_colaboradoras.html')

class LoginView(auth_views.LoginView):
    template_name = 'login.html'