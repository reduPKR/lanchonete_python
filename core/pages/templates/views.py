from django.shortcuts import render

def home(request):
    dados = {
        'title': 'Home-page',
        'header': 'Pagina inicial',
        'icon': 'fas fa-home'
    }
    return render(request, 'home.html', dados)