from django.shortcuts import render, redirect
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
            return redirect(cadastrar_cliente) # Redirecione para uma página de sucesso
    else:
        form = ClienteForm()
    
    return render(request, 'adicionar.html', {'form': form})

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'formulario.html', {'clientes': clientes})