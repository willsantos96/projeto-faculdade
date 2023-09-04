from django.contrib.auth.backends import BaseBackend
from .models import ContaEscola

class ContaEscolaBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            conta_escola = ContaEscola.objects.get(username=username)
            if conta_escola.check_password(password):
                return conta_escola
        except ContaEscola.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return ContaEscola.objects.get(pk=user_id)
        except ContaEscola.DoesNotExist:
            return None
