from django.shortcuts import render, redirect
from django.contrib import messages

from core.dao import Beverage


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

def create_submit(request):
    if request.POST:
        name = request.POST.get('name')
        size = request.POST.get('size')
        value = request.POST.get('value')

        if name:
            if size:
                if value:
                    beverage = Beverage.create(name,size,value)

                    if beverage is None:
                        messages.error(request, "Erro ao cadastrar a bebida")
                else:
                    messages.error(request, "Valor da bebida nao pode estar vazia")
            else:
                messages.error(request, "Tamanho da bebida nao pode estar vazia")
        else:
            messages.error(request, "Nome nao pode estar vazio")
    else:
        messages.error(request, "Erro no rest")

    return redirect('/beverage/create')


def list(request):
    return return_list(request, Beverage.get_all())

def return_list(request, list):
    dados = {
        'title': 'Lista de bebidas',
        'header': 'Lista de bebidas',
        'icon': 'fas fa-glass-martini',
        'beverages': list
    }

    return render(request, 'beverage/list.html', dados)


def filter(request):
    dados = {
        'title': 'Filtragem de bebidas',
        'header': 'Filtragem de bebidas',
        'icon': 'fas fa-glass-martini',
    }

    return render(request, 'beverage/filter.html', dados)

def filter_submit(request):
    if request.GET:
        search = request.GET.get("search")
        if search:
            beverages = Beverage.filter(search)

            if len(beverages) > 0:
                return return_list(request, beverages)
            else:
                messages.error(request, 'Bebida não encontrada')
        else:
            messages.error(request, 'Busca esta vazia')
    else:
        messages.error(request, 'Erro durante a solicitação')

    return redirect('/beverage/filter')


def edit(request,id):
    if id:
        dados = {
            'title': 'Editar bebida',
            'header': 'Editar bebida',
            'icon': 'fas fa-glass-martini',
            'beverage': Beverage.get_by_id(id),
        }

        return render(request, 'beverage/create.html', dados)
    else:
        messages.error(request, "ID nao encontrado")

    return redirect('/beverage/list')


def edit_submit(request):
    if request.POST:
        id = request.POST.get('id')
        name = request.POST.get('name')
        size = request.POST.get('size')
        price = request.POST.get('price')

        if name or size or price:
            beverage = Beverage.update(id, name, size, price)

            if beverage is None:
                messages.error(request, "Erro ao atualizar a bebida")
        else:
            if price is None:
                messages.error(request, "preço nao pode estar vazio")
            if size is None:
                messages.error(request, "Lista de tamanho vazia")
            if name is None:
                messages.error(request, "Nome nao pode estar vazio")

        return redirect('/beverage/edit/{}'.format(id))
    else:
        messages.error(request, "Erro no rest")

    return redirect('/beverage/list')