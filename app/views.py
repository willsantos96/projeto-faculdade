from django.shortcuts import render

def adicionar (request):
    # Lógica para renderizar a página do formulário
    return render(request, 'adicionar.html')

def formulario (request):
    # Lógica para renderizar a página de validação
    return render(request, 'formulario.html')
