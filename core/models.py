from django.db import models

class Ingredients(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'ingredients'

class IngredientValue(models.Model):
    value = models.DecimalField(max_digits=5, decimal_places=2, localize=True)
    date = models.DateField()

    ingredient = models.ForeignKey(Ingredients, on_delete=models.CASCADE)

    class Meta:
        db_table = 'ingredients_value'

