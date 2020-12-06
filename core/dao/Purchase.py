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