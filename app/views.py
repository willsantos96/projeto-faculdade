from django.shortcuts import render, redirect, get_object_or_404
from .forms import ClienteForm
from .models import Cliente


def home (request):
    # Lógica para renderizar a página home
    return render(request, 'home.html')

def adicionar (request):
    # Lógica para renderizar a página do formulário
    return render(request, 'adicionar.html')

def formulario (request):
    # Lógica para renderizar a página de validação
    return render(request, 'formulario.html')


def cadastrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('selecionar_cliente') # Redirecione para uma página de sucesso
    else:
        form = ClienteForm()
    
    return render(request, 'adicionar.html', {'form': form})

def selecionar_cliente(request):
    clientes = Cliente.objects.all()
    return render(request, 'selecionar.html', {'clientes': clientes})


def editar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)

    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('selecionar_cliente')  # Redirecione para uma página de sucesso
    else:
        form = ClienteForm(instance=cliente)
    
    return render(request, 'editar.html', {'form': form})

def selecionar_cliente(request):
    clientes = Cliente.objects.all()
    return render(request, 'selecionar.html', {'clientes': clientes})

def excluir_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('selecionar_cliente')
    
    