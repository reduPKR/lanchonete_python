from django.shortcuts import render

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