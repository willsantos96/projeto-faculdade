from django.shortcuts import render, redirect, get_object_or_404
from .forms import AlunoForm
from .models import Aluno


def home (request):
    # Lógica para renderizar a página home
    return render(request, 'home.html')

def adicionar (request):
    # Lógica para renderizar a página do formulário
    return render(request, 'adicionar.html')

def formulario (request):
    # Lógica para renderizar a página de validação
    return render(request, 'formulario.html')


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
    
    