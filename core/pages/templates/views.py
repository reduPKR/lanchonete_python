from django.shortcuts import render

def home(request):
    dados = {
        'title': 'Home-page',
        'header': 'Pagina inicial'
    }
    return render(request, 'home.html', dados)