from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from .forms import AlunoForm
from .forms import ContaEscolaForm
from .models import Aluno
import logging


def home (request):
    # Lógica para renderizar a página home
    return render(request, 'home.html')

def login_escola (request):
    # Lógica para renderizar a página de login da escola
    return render(request, 'login_escola.html')

def formulario (request):
    # Lógica para renderizar a página de validação
    return render(request, 'formulario.html')


def login_escola(request):
    logger = logging.getLogger(__name__)  # Configurar o logger

    if request.method == 'POST':
        form = ContaEscolaForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password'] 
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                logger.info("Usuário autenticado com sucesso: %s", username)
                return redirect('cadastrar_aluno')
            else:
                logger.warning("Falha na autenticação para o usuário: %s", username)
    else:
        form = ContaEscolaForm()
    
    context = {'form': form}
    return render(request, 'login_escola.html', context)


def criar_contaescola(request):
    if request.method == 'POST':
        form = ContaEscolaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_escola') # Redirecione para uma página de sucesso
    else:
        form = ContaEscolaForm()

    context = {'form': form}
    return render(request, 'form_escola.html', context)


def cadastrar_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('selecionar_aluno') # Redirecione para uma página de sucesso
    else:
        form = AlunoForm()
    
    context = {'form': form}
    return render(request, 'adicionar.html', context)

def selecionar_aluno(request):
    alunos = Aluno.objects.all()
    return render(request, 'selecionar.html', {'alunos': alunos})


def editar_aluno(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)

    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect('selecionar_cliente')  # Redirecione para uma página de sucesso
    else:
        form = AlunoForm(instance=aluno)
    
    return render(request, 'editar.html', {'form': form})

def selecionar_aluno(request):
    alunos = Aluno.objects.all()
    return render(request, 'selecionar.html', {'alunos': alunos})

def excluir_aluno(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    if request.method == 'POST':
        aluno.delete()
        return redirect('selecionar_aluno')
    
    