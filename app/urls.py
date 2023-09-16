from django.urls import path
from . import views  # Importe as funções de visualização da sua aplicação
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.home, name='home'),  # URL para a página home
    path('cadastrar_aluno/', views.cadastrar_aluno, name='cadastrar_aluno'),
    path('selecionar/', views.selecionar_aluno, name='selecionar_aluno'),
    path('editar/<int:pk>/', views.editar_aluno, name='editar_aluno'),
    path('excluir/<int:pk>/', views.excluir_aluno, name='excluir_aluno'),
    path('criar_contaescola/', views.criar_contaescola, name='criar_contaescola'),
    path('login_escola/', views.login_escola, name='login_escola'),
    path('logout/', views.fazer_logout, name='logout'),

    path('area_aluno/', views.area_aluno, name='area_aluno'),
]
