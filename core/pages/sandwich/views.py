from django.shortcuts import render, redirect
from django.contrib import messages

from core.dao import Sandwich, Ingredient

def menu(request):
    dados = {
        'title': 'Menu de lanches',
        'header': 'Menu de lanches',
        'icon': 'fas fa-hamburger'
    }
    return render(request, 'sandwich/menu.html', dados)

def create(request):
    dados = {
        'title': 'Criação de lanches',
        'header': 'Novo lanche',
        'icon': 'fas fa-hamburger',
        'ingredients': Ingredient.get_all_with_price()
    }

    return render(request, 'sandwich/create.html', dados)

def create_submit(request):
    if request.POST:
        name = request.POST.get('name')
        ingredient_list = request.POST.get('ingredient_list')
        profit = request.POST.get('percent')

        if name:
            if ingredient_list:
                if profit:
                    list = ingredient_list.split(',')
                    sandwich = Sandwich.create(name,profit,list)

                    if sandwich is None:
                        messages.error(request, "Erro ao cadastrar o lanche")
                else:
                    messages.error(request, "Percentual de lucro nao pode estar vazio")
            else:
                messages.error(request, "Lista de ingredientes vazia")
        else:
            messages.error(request, "Nome nao pode estar vazio")
    else:
        messages.error(request,"Erro no rest")

    return redirect('/sandwich/create')

def list(request):
    return return_list(request, Sandwich.get_all())

def return_list(request, list):
    dados = {
        'title': 'Lista de lanches',
        'header': 'Lista de lanches',
        'icon': 'fas fa-hamburger',
        'sandwichs': list
    }

    return render(request, 'sandwich/list.html', dados)