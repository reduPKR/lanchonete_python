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

