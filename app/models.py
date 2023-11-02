from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission


class AcessoAlunoManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('O campo username é obrigatório.')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, password, **extra_fields)

class AcessoAluno(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)
    is_staff = models.BooleanField(default=False)
    groups = models.ManyToManyField(Group, blank=True, related_name='acessoaluno_user_set')
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='acessoaluno_user_set')
    objects = AcessoAlunoManager()

    def delete(self, using=None, keep_parents=False):
        # Limpe as chaves estrangeiras manualmente
        for group in self.groups.all():
            group.acessoaluno_user_set.remove(self)
        for permission in self.user_permissions.all():
            permission.acessoaluno_user_set.remove(self)
        return super().delete(using=using, keep_parents=keep_parents)


    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username



class ContaEscolaManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('O campo username é obrigatório.')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, password, **extra_fields)

class ContaEscola(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128) 

    # Adicione related_name para evitar conflitos
    groups = models.ManyToManyField(Group, blank=True, related_name='contaescola_user_set')
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='contaescola_user_set')
    is_staff = models.BooleanField(default=False)

    objects = ContaEscolaManager()


    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username
    
    
class Aluno(models.Model):
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    ]

    NIVEL_ENSINO_CHOICES = [
        ('Fundamental', 'Fundamental'),
        ('Médio', 'Médio'),
        ('Superior', 'Superior'),
    ]

    nome = models.CharField(max_length=100)
    email = models.EmailField()
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=14)  # Pode ser ajustado para usar um campo de CPF personalizado
    rg = models.CharField(max_length=20)
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=255)
    numero = models.CharField(max_length=20)
    complemento = models.CharField(max_length=100, blank=True)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    cep = models.CharField(max_length=10)
    uf = models.CharField(max_length=2)

    nome_mae = models.CharField(max_length=100)
    nome_pai = models.CharField(max_length=100)
    rg_responsavel = models.CharField(max_length=20)
    codigo_escola = models.CharField(max_length=20)
    nome_escola = models.CharField(max_length=255)
    matricula_escolar = models.CharField(max_length=20)
    nivel_ensino = models.CharField(max_length=20, choices=NIVEL_ENSINO_CHOICES)
    serie = models.CharField(max_length=20)
    codigo_curso = models.CharField(max_length=20)


    linha1 = models.TextField(blank=True)
    linha2 = models.TextField(blank=True)
    linha3 = models.TextField(blank=True)
    linha4 = models.TextField(blank=True)
    linha5 = models.TextField(blank=True)
    linha6 = models.TextField(blank=True)
    linha7 = models.TextField(blank=True)
    linha8 = models.TextField(blank=True)
    linha9 = models.TextField(blank=True)
    linha10 = models.TextField(blank=True)

    def __str__(self):
            return self.nome

