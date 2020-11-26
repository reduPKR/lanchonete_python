from django.shortcuts import render, redirect
from django.contrib import messages

from core.dao import Beverage


def menu(request):
    dados = {
        'title': 'Menu de bebidas',
        'header': 'Menu de bebidas',
        'icon': 'fas fa-glass-martini'
    }
    return render(request, 'beverage/menu.html', dados)


def create(request):
    dados = {
        'title': 'Cadastrar bebidas',
        'header': 'Cadastro de bebida',
        'icon': 'fas fa-glass-martini'
    }

    return render(request, 'beverage/create.html', dados)

def create_submit(request):
    if request.POST:
        name = request.POST.get('name')
        size = request.POST.get('size')
        value = request.POST.get('value')

        if name:
            if size:
                if value:
                    beverage = Beverage.create(name,size,value)

                    if beverage is None:
                        messages.error(request, "Erro ao cadastrar a bebida")
                else:
                    messages.error(request, "Valor da bebida nao pode estar vazia")
            else:
                messages.error(request, "Tamanho da bebida nao pode estar vazia")
        else:
            messages.error(request, "Nome nao pode estar vazio")
    else:
        messages.error(request, "Erro no rest")

    return redirect('/beverage/create')


def list(request):
    dados = {
        'title': 'Lista de bebidas',
        'header': 'Lista de bebidas',
        'icon': 'fas fa-glass-martini',
        'beverages': Beverage.get_all()
    }

    return render(request, 'beverage/list.html', dados)


def filter(request):
    return None


def filter_submit(request):
    return None