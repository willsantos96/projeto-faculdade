from .models import AcessoAluno, ContaEscola

def tipo_usuario(request):
    usuario = request.user

    if usuario.is_authenticated:
        if isinstance(usuario, AcessoAluno):
            return {'tipo_usuario': 'Aluno'}
        elif isinstance(usuario, ContaEscola):
            return {'tipo_usuario': 'Escola'}

    return {'tipo_usuario': None}
