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
        add_profit(sandwich, profit)
        prepare_list(sandwich, list)

        return sandwich
    else:
        return None

def prepare_list(sandwich, list):
    for item in list:
        name_sandwich = item.split(" - ")
        sandwich_recipe(sandwich, name_sandwich[0])

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

def get_by_name(name):
    sandwich = models.Sandwich.objects.get(name=name)
    return get_by_id(sandwich.id)

def get_by_id(id):
    try:
        return try_get_by_id(id)
    except:
        return None

def try_get_by_id(id):
    sandwich = models.Sandwich.objects.get(id=id)

    sandwich.profit = get_profit(sandwich)
    sandwich.price = sandwich_price(sandwich)
    sandwich.ingredients = sandwich_ingredients(sandwich)

    return sandwich

def sandwich_ingredients(sandwich):
    return models.SandwichIngredient.objects.filter(sandwich=sandwich)

def update(id, name, profit, list):
    try:
        return try_update(id, name, profit, list)
    except:
        return None

def try_update(id, name, profit, list):
    update_name(id, name)

    sandwich = models.Sandwich.objects.get(id=id)
    prepare_list(sandwich, list)

    if validade_profit(sandwich, profit):
        add_profit(sandwich, profit)

    return True

def update_name(id, name):
    models.Sandwich.objects.filter(id=id).update(name=name)

def validade_profit(sandwich, profit):
    value = models.SandwichValue.objects.filter(sandwich=sandwich).last()

    if float(value.percent) == float(profit):
        return False
    else:
        return True

def add_profit(sandwich, profit):
    models.SandwichValue.objects.create(
        percent=profit,
        sandwich=sandwich,
        date=date.today()
    )

def get_profit(sandwich):
    try:
        return models.SandwichValue.objects.filter(sandwich=sandwich).last()
    except:
        return None


def remove_ingredient(sandwich_id, ingredient_id):
    try:
        try_remove_ingredient(sandwich_id, ingredient_id)
        return True
    except:
        return None

def try_remove_ingredient(sandwich_id, ingredient_id):
    sandwich = get_by_id(sandwich_id)
    ingredient = Ingredient.get_by_id(ingredient_id)

    if sandwich and ingredient:
        models.SandwichIngredient.objects.get(
            ingredient=ingredient,
            sandwich=sandwich
        ).delete()


def filter(search):
    sandwichs = list(models.Sandwich.objects.filter(name__contains=search))

    ingredients = Ingredient.filter(search)
    for ingredient in ingredients:
        itens = models.SandwichIngredient.objects.filter(ingredient=ingredient)

        for item in itens:
            if item.sandwich not in sandwichs:
                sandwichs.append(item.sandwich)

    return sandwichs


