from django.urls import path
from . import views  # Importe as funções de visualização da sua aplicação

urlpatterns = [
    path('', views.home, name='home'),  # URL para a página home
    path('cadastrar_clientes/', views.cadastrar_cliente, name='cadastrar_cliente'),
    path('lista_clientes/', views.lista_clientes, name='lista_clientes'),    # URL para a página de validação do aluno
    path('selecionar/', views.selecionar_cliente, name='selecionar_cliente'),
    path('editar/<int:pk>/', views.editar_cliente, name='editar_cliente'),
]
