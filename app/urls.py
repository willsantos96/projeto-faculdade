from django.urls import path
from . import views  # Importe as funções de visualização da sua aplicação

urlpatterns = [
    path('', views.home, name='home'),  # URL para a página home
    path('cadastrar_clientes/', views.cadastrar_cliente, name='cadastrar_cliente'),
    path('selecionar/', views.selecionar_cliente, name='selecionar_cliente'),
    path('editar/<int:pk>/', views.editar_cliente, name='editar_cliente'),
    path('excluir/<int:pk>/', views.excluir_cliente, name='excluir_cliente'),
]
