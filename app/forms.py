from django import forms
from .models import Aluno
from .models import ContaEscola
from .models import AcessoAluno
from django.contrib.auth.hashers import make_password


class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = '__all__'


#--------------------------------------------------------#

class ContaEscolaForm(forms.ModelForm):
    class Meta:
        model = ContaEscola
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }

    def save(self, commit=True):
        contaescola = super().save(commit=False)
        contaescola.password = make_password(self.cleaned_data['password'])
        if commit:
            contaescola.save()
        return contaescola

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)

#---------------------------------------------------------#

class AcessoAlunoForm(forms.ModelForm):
    class Meta:
        model = AcessoAluno
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }

    def save(self, commit=True):
        acessoaluno = super().save(commit=False)
        acessoaluno.password = make_password(self.cleaned_data['password'])
        if commit:
            acessoaluno.save()
        return acessoaluno


class AcessoAlunoLoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)