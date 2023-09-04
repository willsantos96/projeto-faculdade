from django.shortcuts import render, redirect, get_object_or_404
from .forms import AlunoForm
from .forms import ContaEscolaForm
from .models import Aluno
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required




def home (request):
    # Lógica para renderizar a página home
    return render(request, 'home.html')

def formulario (request):
    # Lógica para renderizar a página de validação
    return render(request, 'formulario.html')

@csrf_protect
def login_escola(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                # Redirecione para a página de sucesso ou qualquer outra página desejada
                return redirect('cadastrar_aluno')
            else:
                # Autenticação falhou, exiba uma mensagem de erro no template
                return render(request, 'login_escola.html', {'form': form, 'error_message': 'Credenciais inválidas'})
    else:
        form = LoginForm()

    return render(request, 'login_escola.html', {'form': form})


def fazer_logout(request):
    logout(request)
    return redirect('login_escola')

    
@csrf_protect
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


@login_required(login_url='/login_escola/')
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
    
    