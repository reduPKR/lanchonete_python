from core import models
from datetime import date

from core.dao import Ingredient

def create(name, profit, list):
    try:
        return try_create(name, profit, list)
    except:
        return None

def try_create(name, profit, list):
    sandwich_test = models.Sandwich.objects.filter(name=name)

    if len(sandwich_test) == 0:
        sandwich = models.Sandwich.objects.create(name=name)
        models.SandwichValue.objects.create(
            percent=profit,
            sandwich=sandwich,
            date=date.today()
        )

        sandwich = models.Sandwich.objects.get(id=2)
        for item in list:
            name_sandwich = item.split(" - ")
            sandwich_recipe(sandwich, name_sandwich[0])
        return sandwich
    else:
        return None

def sandwich_recipe(sandwich, ingredient_name):
    ingredient = Ingredient.get_by_name(ingredient_name)

    if ingredient:
        models.SandwichIngredient.objects.create(
            sandwich=sandwich,
            ingredient=ingredient
        )

def get_all():
    try:
        sandwichs = models.Sandwich.objects.all().order_by('name')

        for item in sandwichs:
            item.price = sandwich_price(item)

        return sandwichs
    except:
        return None

def sandwich_price(sandwich):
    ingredients = models.SandwichIngredient.objects.filter(sandwich=sandwich)
    profit = models.SandwichValue.objects.filter(sandwich=sandwich).last()
    percent = profit.percent/100

    price = 0
    for item in ingredients:
        ingredient_value = models.IngredientValue.objects.filter(ingredient=item.ingredient).last()
        price += ingredient_value.value

    return round(float(price) + (float(price)*percent), 2)
