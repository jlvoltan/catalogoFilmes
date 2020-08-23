from django import forms
from serie.models import Serie


class SerieFormulario(forms.ModelForm):
    class Meta: #Uma subclasse
        model = Serie
        fields = '__all__'