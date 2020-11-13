from core import models

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


def update(id, name):
    try:
        return models.Ingredient.objects.filter(id=id).update(name=name)
    except:
        return None