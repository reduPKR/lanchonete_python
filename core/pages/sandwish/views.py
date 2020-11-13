from django.shortcuts import render, redirect
from django.contrib import messages

def menu(request):
    dados = {
        'title': 'Menu de lanches',
        'header': 'Menu de lanches',
        'icon': 'fas fa-hamburger'
    }
    return render(request, 'sandwish/menu.html', dados)