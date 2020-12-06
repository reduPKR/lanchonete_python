from django.shortcuts import render, redirect
from django.contrib import messages

from core.dao import Sandwich

def menu(request):
    dados = {
        'title': 'Menu',
        'header': 'Menu',
        'icon': 'fas fa-hamburger'
    }
    return render(request, 'purchase/menu.html', dados)

# def create(request):
#     dados = {
#         'title': 'Criação de lanches',
#         'header': 'Novo lanche',
#         'icon': 'fas fa-hamburger',
#         'ingredients': Ingredient.get_all_with_price()
#     }
#
#     return render(request, 'purchase/create.html', dados)

