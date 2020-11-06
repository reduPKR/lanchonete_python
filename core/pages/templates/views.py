from django.shortcuts import render

def home(request):
    dados = {
        'title': 'Home-page',
        'header': 'Lanchonete',
        'icon': 'fas fa-store'
    }
    return render(request, 'home.html', dados)