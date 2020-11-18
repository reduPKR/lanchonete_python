from django.shortcuts import render, redirect
from django.contrib import messages

import core.dao.Ingredient as Ingredient

def menu(request):
    dados = {
        'title': 'Menu de lanches',
        'header': 'Menu de lanches',
        'icon': 'fas fa-hamburger'
    }
    return render(request, 'sandwish/menu.html', dados)


def create(request):
    dados = {
        'title': 'Criação de lanches',
        'header': 'Novo lanche',
        'icon': 'fas fa-hamburger',
        'ingredients': Ingredient.get_all()
    }
    return render(request, 'sandwish/create.html', dados)


def create_submit(request):
    if request.POST:
        name = request.POST.get('name')
        ingredient_list = request.POST.get('ingredient_list')

        if name:
            if ingredient_list:
                list = ingredient_list.split(',')
            else:
                messages.error(request, "Lista de ingredientes vazia")
        else:
            messages.error(request, "Nome nao pode estar vazio")
    else:
        messages.error(request,"Erro no rest")

    return redirect('/sandwish/create')