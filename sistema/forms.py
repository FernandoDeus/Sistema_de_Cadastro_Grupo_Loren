from django.forms import ModelForm
from sistema.models import cadastro

# Create the form class.
class cadastroform(ModelForm):
    class Meta:
        model = cadastro
        fields = ['nome_projeto', 'data_inicio', 'data_termino', 'valor_projeto', 'participante']
