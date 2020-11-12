from django.shortcuts import render, redirect
from django.contrib import messages

import core.dao as dao

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
            ingredient = dao.Ingredient.get_by_name(name)

            if ingredient is None:
                pass
            else:
                messages.error(request, 'Ingrediente com mesmo nome ja cadastrado')
        else:
            messages.error(request, 'Nome não pode estar em branco')
    else:
        messages.error(request, 'Erro durante envio')

    return redirect('/ingredient/create')