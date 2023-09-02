from django.contrib.auth.backends import ModelBackend
from .models import ContaEscola

class ContaEscolaBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            account = ContaEscola.objects.get(username=username)
            if account.check_password(password):
                return account
        except ContaEscola.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return ContaEscola.objects.get(pk=user_id)
        except ContaEscola.DoesNotExist:
            return None
