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

        for item in list:
            sandwich_recipe(sandwich, item)
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
        return models.Sandwich.objects.all().order_by('name')
    except:
        return None