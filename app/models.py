from django.db import models

class Cliente(models.Model):
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    ]

    nome = models.CharField(max_length=100)
    email = models.EmailField()
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=14)
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome
