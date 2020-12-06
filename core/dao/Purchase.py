from core import models
import datetime

from core.dao import Sandwich

def create(list):
    try:
        return try_create(list)
    except:
        return None

def try_create(list):
    if len(list) > 0:
        code_id = 1

        code = models.Purchase.objects.all().last()
        if code is not None:
            code_id = code.id + 1

        purchase = models.Purchase.objects.create(
            code = code_id,
            date=datetime.date.today()
        )

        for item in list:
            name = item.split(' - ')
            sandwich = Sandwich.get_by_name(name[0])

            models.SandwichOrder.objects.create(
                sandwich=sandwich,
                purchase=purchase
            )

        return purchase
    else:
        return None

def get_all_open():
    purchases = models.Purchase.objects.filter(open=True)

    for item in purchases:
        sandwichs = models.SandwichOrder.objects.filter(purchase=item)

        price = 0

        for sandwich in sandwichs:
            price = price + Sandwich.sandwich_price(sandwich.sandwich)

        item.price = round(price)

    return purchases

def close(id):
    try:
        return try_close(id)
    except:
        return None

def try_close(id):
    models.Purchase.objects.filter(id=id).update(open=False);
    return True