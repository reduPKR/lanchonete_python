from django.shortcuts import render

def menu(request):
    dados = {
        'title': 'Menu de bebidas',
        'header': 'Menu de bebidas',
        'icon': 'fas fa-glass-martini'
    }
    return render(request, 'beverage/menu.html', dados)