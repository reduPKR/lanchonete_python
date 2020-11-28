from core import models
from datetime import date

def create(name, size, value):
    try:
        return try_create(name, size, value)
    except:
        return None

def try_create(name, size, value):
    beverage = models.Beverage.objects.create(name=name, size=size)
    add_price(beverage, value)

    return beverage

def add_price(beverage, value):
    models.BeverageValue.objects.create(
        beverage=beverage,
        value=value,
        date=date.today()
    )

def get_all():
    try:
        return try_get_all()
    except:
        return None

def try_get_all():
    beverages = models.Beverage.objects.all().order_by("name")

    for item in beverages:
        item.price = get_price(item)

    return beverages

def get_price(beverage):
    beverage = models.BeverageValue.objects.filter(beverage=beverage).last()
    return beverage.value

def filter(search):
    try:
        return try_filter(search)
    except:
        return None

def try_filter(search):
    beverages = models.Beverage.objects.filter(name__contains=search).order_by("name")

    for item in beverages:
        item.price = get_price(item)

    return beverages

def get_by_id(id):
    try:
        return try_get_by_id(id)
    except:
        return None

def try_get_by_id(id):
    beverage = get_beverage_by_id(id)
    beverage.price = get_price(beverage)

    return beverage

def get_beverage_by_id(id):
    return models.Beverage.objects.get(id=id)

def update_name(id, name):
    models.Beverage.objects.filter(id=id).update(name=name)

def update_size(id, size):
    models.Beverage.objects.filter(id=id).update(size=size)

def validade_price(beverage, price):
    value = models.BeverageValue.objects.filter(beverage=beverage).last()

    if float(value.value) == float(price):
        return False
    else:
        return True

def update(id, name, size, price):
    try:
        return try_update(id, name, size, price)
    except:
        return None

def try_update(id, name, size, price):
    update_name(id, name)
    update_size(id, size)

    beverage = models.Beverage.objects.get(id=id)
    if validade_price(beverage, price):
        add_price(beverage, price)

    return True