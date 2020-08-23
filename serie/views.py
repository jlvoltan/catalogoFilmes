from django.shortcuts import render
from django.http import HttpResponseNotAllowed
from . import forms, models

# Create your views here.
def cadastrar(request):
    form = forms.SerieFormulario()
    if request.method == 'POST':    #Verifico o método do request
        form = forms.SerieFormulario(request.POST)
        if form.is_valid(): form.save(commit=True) #Vejo se é válido, salvo já fazendo um commit.
        else: print("ERRO ao salvar. Dado não válido.")

#Precisamos renderizar a tela com as novas info adicionadas
    lista_series = models.Serie.objects.order_by('nome')
    data_dict = {"serie_registro":lista_series,'form':form}
    return render(request, 'serie/serie.html', data_dict)



###### DELETE ##########
def delete(request,id):
    try:
        models.Serie.objects.filter(id=id).delete()
        form = forms.SerieFormulario()
        lista_series = models.Serie.objects.order_by('nome')  # Os generos são salvos ordenados em uma lista
        data_dict = {'form': form, 'serie_registro': lista_series}
        return render(request, 'serie/serie.html', data_dict)
    except:
        return HttpResponseNotAllowed()

#######  UPDATE  #############
def update(request,id):
    item = models.Serie.objects.get(id=id);
    if request.method == "GET":
        form =forms.SerieFormulario(initial={'nome': item.nome})
        data_dict = {'form':form}
        return render(request,'serie/serie_update.html',data_dict)
    else:
        form = forms.SerieFormulario(request.POST)
        item.nome = form.data['nome']
        item.save()
        lista_series = models.Serie.objects.order_by('nome')  # As séries são salvos ordenados em uma lista
        data_dict = {'form': form, 'serie_registro': lista_series}
        return render(request, 'serie/serie.html', data_dict)
