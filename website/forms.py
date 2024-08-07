from django import forms
from .models import Funcionario

class InsereFuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = [
            'nome',
            'sobre_nome',
            'cpf',
            'remuneracao',
            'tempo_de_servico',
        ]

    