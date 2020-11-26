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