from django.shortcuts import render, redirect
from django.contrib import messages

from core.dao import Sandwich, Purchase

def menu(request):
    dados = {
        'title': 'Menu',
        'header': 'Menu',
        'icon': 'fas fa-hamburger'
    }
    return render(request, 'purchase/menu.html', dados)

def create(request):
    dados = {
        'title': 'Novo pedido',
        'header': 'Novo pedido',
        'icon': 'fas fa-hamburger',
        'sandwichs': Sandwich.get_all()
    }

    return render(request, 'purchase/create.html', dados)

def create_submit(request):
    if request.POST:
        sandwich_list = request.POST.get('sandwich_list')
        print(sandwich_list)

        if sandwich_list:
            list = sandwich_list.split(',')
            purchase = Purchase.create(list)

            if purchase is None:
                messages.error(request, "Erro ao cadastrar o lanche")
        else:
            messages.error(request, "Lista de lanches vazia")
    else:
        messages.error(request,"Erro no rest")

    return redirect('/purchase/create')