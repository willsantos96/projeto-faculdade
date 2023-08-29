from django.urls import path
from . import views  # Importe as funções de visualização da sua aplicação

urlpatterns = [
    path('', views.home, name='home'),  # URL para a página home
    path('cadastrar_aluno/', views.cadastrar_aluno, name='cadastrar_aluno'),
    path('selecionar/', views.selecionar_aluno, name='selecionar_aluno'),
    path('editar/<int:pk>/', views.editar_aluno, name='editar_aluno'),
    path('excluir/<int:pk>/', views.excluir_aluno, name='excluir_aluno'),
]
