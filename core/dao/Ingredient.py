from core import models
import datetime

def create(name):
    try:
        return models.Ingredient.objects.create(
            name=name
        )
    except:
        return None


def get_by_name(name):
    try:
        return models.Ingredient.objects.get(
            name=name
        )
    except:
        return None

def get_all():
    try:
        return models.Ingredient.objects.all().order_by('name')
    except:
        return None


def filter(name):
    try:
        return models.Ingredient.objects.filter(
            name__contains=name
        ).order_by('name')
    except:
        return []


def get_by_id(id):
    try:
        return models.Ingredient.objects.get(
            id=id
        )
    except:
        return None


def update(id, name, price):
    update_name(id, name)

    ingredient = models.Ingredient.objects.filter(id=id).first()
    value = models.IngredientValue.objects.filter(ingredient=ingredient).last()
    update_price(value.id, price)


def update_name(id, name):
    try:
        return models.Ingredient.objects.filter(id=id).update(name=name)
    except:
        return None

def update_price(id, price):
    try:
        return models.IngredientValue.objects.filter(id=id).update(value=price)
    except:
        return None


def set_value(ingredient, price):
    try:
        return models.IngredientValue.objects.create(
            ingredient=ingredient,
            value=price,
            date=datetime.date.today()
        )
    except:
        return None

def get_value(ingredient):
    try:
        return models.IngredientValue.objects.filter(ingredient=ingredient).last()
    except:
        return None

def get_info_by_id(id):
    try:
        ingredient = get_by_id(id)
        ingredient.price = get_value(ingredient)
        return ingredient
    except:
        return None
