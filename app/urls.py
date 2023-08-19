from django.urls import path
from . import views  # Importe as funções de visualização da sua aplicação

urlpatterns = [
    path('adicionar/', views.adicionar, name='adicionar'),  # URL para a página de adicionar aluno
    path('formulario/', views.formulario, name='formulario'),    # URL para a página de validação do aluno
]
