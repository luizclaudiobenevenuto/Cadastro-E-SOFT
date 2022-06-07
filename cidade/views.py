from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import CadastroModelForm
from .models import Cadastro


def index(request):
    context = {
        'Cadastros': Cadastro.objects.all(),
        'title': 'Lista de Endereços'
    }
    return render(request, 'lista.html', context)


def manage_data(form):
    if not form.cleaned_data.get('id', False):
        form.save()
        return

    cadastro = Cadastro.objects.get(id=form.cleaned_data['id'])
    cadastro.cep = form.cleaned_data['cep']
    cadastro.cidade = form.cleaned_data['cidade']
    cadastro.endereco = form.cleaned_data['endereco']
    cadastro.numero = form.cleaned_data['numero']
    cadastro.complemento = form.cleaned_data['complemento']
    cadastro.bairro = form.cleaned_data['bairro']
    cadastro.uf = form.cleaned_data['uf']
    cadastro.descricao = form.cleaned_data['descricao']
    cadastro.save()


def cadastro(request):
    form = CadastroModelForm()
    if request.method == 'POST':
        form = CadastroModelForm(request.POST)
        if form.is_valid():
            manage_data(form)
            return redirect(reverse('index'))

    context = {
        'form': form,
        'botao': 'Cadastrar',
        'title': 'Cadastro de Endereço'
    }
    return render(request, 'cadastro.html', context)


def update(request, id):
    cadastro = Cadastro.objects.get(id=id)
    form = CadastroModelForm(request.POST or None, instance=cadastro)
    context = {
        'form': form,
        'botao': 'Atualizar',
        'title': 'Atualização de Endereço'
    }
    return render(request, 'cadastro.html', context)
