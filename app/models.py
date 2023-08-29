from django.db import models
from django import forms


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

