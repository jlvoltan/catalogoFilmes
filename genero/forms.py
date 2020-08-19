#ideia de criar uma classe a ser usada no formulário
from genero.models import GeneroFormulario
from django import forms

""" Deixou de utilizar isso quando criou a classe models.py
class GeneroFormulario(forms.Form):
    def __init__(self, *args, **kwargs):
        super(GeneroFormulario, self).__init__(*args,**kwargs)
        self.fields['descricao'].error_messages = {'required':'Campo de preenchimento OBRIGATÓRIO'}

    descricao = forms.CharField(label= "Gênero do Filme", required=True) #required, Pra dizer que é obrigatório
"""

class GeneroFormulario(forms.ModelForm):
    class Meta:
        model = GeneroFormulario
        fields = '__all__'   # aqui que podemos selecionar os campos
