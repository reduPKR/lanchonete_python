from django.shortcuts import render

def menu(request):
    dados = {
        'title': 'Menu de ingredientes',
        'header': 'Menu de ingredientes',
        'icon': 'fas fa-store'
    }
    return render(request, 'ingredient/menu.html', dados)