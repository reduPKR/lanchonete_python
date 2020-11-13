from django.shortcuts import render, redirect
from django.contrib import messages

import core.dao.Ingredient as Ingredient

def menu(request):
    dados = {
        'title': 'Menu de ingredientes',
        'header': 'Menu de ingredientes',
        'icon': 'fas fa-bacon'
    }
    return render(request, 'ingredient/menu.html', dados)

def create(request):
    dados = {
        'title': 'Cadastrar novo ingrediente',
        'header': 'Cadastrar novo ingrediente',
        'icon': 'fas fa-bacon'
    }
    return render(request, 'ingredient/create.html', dados)


def create_submit(request):
    if request.POST:
        name = request.POST.get("name")
        if name:
            ingredient = Ingredient.get_by_name(name)

            if ingredient is None:
                Ingredient.create(name)
            else:
                messages.error(request, 'Ingrediente com mesmo nome ja cadastrado')
        else:
            messages.error(request, 'Nome não pode estar em branco')
    else:
        messages.error(request, 'Erro durante envio')

    return redirect('/ingredient/menu')


def list(request):
    dados = {
        'title': 'Lista de ingredientes',
        'header': 'Lista de ingredientes',
        'icon': 'fas fa-bacon',
        'ingredients': Ingredient.get_all()
    }

    return render(request, 'ingredient/list.html', dados)


def filter(request):
    dados = {
        'title': 'Filtragem de ingredientes',
        'header': 'Filtragem de ingredientes',
        'icon': 'fas fa-bacon'
    }

    return render(request, 'ingredient/filter.html', dados)