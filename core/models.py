from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'ingredient'

class IngredientValue(models.Model):
    value = models.DecimalField(max_digits=5, decimal_places=2, localize=True)
    date = models.DateField()

    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)

    class Meta:
        db_table = 'ingredient_value'

class Sandwich(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'sandwich'

class SandwichValue(models.Model):
    value = models.DecimalField(max_digits=5, decimal_places=2, localize=True)
    date = models.DateField()

    sandwich = models.ForeignKey(Sandwich, on_delete=models.CASCADE)

    class Meta:
        db_table = 'sandwich_value'

class SandwichIngredient(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    sandwich = models.ForeignKey(Sandwich, on_delete=models.CASCADE)

    class Meta:
        db_table = 'sandwich_ingredient'

class Beverage(models.Model):
    name = models.CharField(max_length=50)
    size = models.CharField(max_length=10)

    class Meta:
        db_table = 'beverage'

class BeverageValue(models.Model):
    value = models.DecimalField(max_digits=5, decimal_places=2, localize=True)
    date = models.DateField()

    beverage = models.ForeignKey(Beverage, on_delete=models.CASCADE)

    class Meta:
        db_table = 'beverage_value'



