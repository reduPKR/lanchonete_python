from core import models

def create(name):
    try:
        return models.Ingredient.objects.create(
            name=name
        )
    except:
        return None