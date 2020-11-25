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