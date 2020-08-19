from django.shortcuts import render
from django.http import HttpResponseNotAllowed
from . import forms
from . import models


def cadastro(request):
    if request.method == 'POST':
        form = forms.GeneroFormulario(request.POST)
        if form.is_valid():form.save(commit=True)
        else: print("Erro no valor passado!")
    else: form = forms.GeneroFormulario()

    lista_generos = models.GeneroFormulario.objects.order_by('descricao') #Os generos são salvos ordenados em uma lista
    data_dict = {'form':form, 'generos_registro':lista_generos}
    return render(request,'genero/genero.html', data_dict)

def delete(request,id):
    try:
        models.GeneroFormulario.objects.filter(id=id).delete()
        form = forms.GeneroFormulario()
        lista_generos = models.GeneroFormulario.objects.order_by('descricao')  # Os generos são salvos ordenados em uma lista
        data_dict = {'form': form, 'generos_registro': lista_generos}
        return render(request, 'genero/genero.html', data_dict)
    except:
        return HttpResponseNotAllowed()

def update(request,id):
    item = models.GeneroFormulario.objects.get(id=id);
    if request.method == "GET":
        form =forms.GeneroFormulario(initial={'descricao': item.descricao})
        data_dict = {'form':form}
        return render(request,'genero/genero_update.html',data_dict)
    else:
        form = forms.GeneroFormulario(request.POST)
        item.descricao = form.data['descricao']
        item.save()
        lista_generos = models.GeneroFormulario.objects.order_by('descricao')  # Os generos são salvos ordenados em uma lista
        data_dict = {'form': form, 'generos_registro': lista_generos}
        return render(request, 'genero/genero.html', data_dict)