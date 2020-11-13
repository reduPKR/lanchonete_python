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
        'icon': 'fas fa-bacon',
        'ingredient': None
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
    return return_list(request, Ingredient.get_all())

def return_list(request, list):
    dados = {
        'title': 'Lista de ingredientes',
        'header': 'Lista de ingredientes',
        'icon': 'fas fa-bacon',
        'ingredients': list
    }

    return render(request, 'ingredient/list.html', dados)

def filter(request):
    dados = {
        'title': 'Filtragem de ingredientes',
        'header': 'Filtragem de ingredientes',
        'icon': 'fas fa-bacon'
    }

    return render(request, 'ingredient/filter.html', dados)

def filter_submit(request):
    if request.GET:
        name = request.GET.get("name")
        if name:
            ingredients = Ingredient.filter(name)

            if len(ingredients) > 0:
                return return_list(request, ingredients)
            else:
                messages.error(request, 'Ingrediente nao encontrado')
        else:
            messages.error(request, 'Nome não pode estar em branco')
    else:
        messages.error(request, 'Erro durante a solicitação')

    return redirect('/ingredient/filter')

def edit(request, id):
    if id:
        dados = {
            'title': 'Atualizar ingrediente',
            'header': 'Atualizar ingrediente',
            'icon': 'fas fa-bacon',
            'ingredient': Ingredient.get_by_id(id)
        }

        return render(request, 'ingredient/create.html', dados)
    else:
        messages.error(request, "Erro no envio")

def edit_submit(request):
    return None