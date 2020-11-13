from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'ingredient'

class IngredientValue(models.Model):
    value = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateField()

    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)

    class Meta:
        db_table = 'ingredient_value'

class Sandwich(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'sandwich'

class SandwichValue(models.Model):
    percent = models.FloatField(default=5)
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
    value = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateField()

    beverage = models.ForeignKey(Beverage, on_delete=models.CASCADE)

    class Meta:
        db_table = 'beverage_value'

class Purchase(models.Model):
    code = models.IntegerField()
    date = models.DateField()

    open = models.BooleanField(default=True)

    class Meta:
        db_table = 'purchase'

class BeverageOrder(models.Model):
    beverage = models.ForeignKey(Beverage, on_delete=models.CASCADE)
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)

    class Meta:
        db_table = 'beverage_order'

class SandwichOrder(models.Model):
    sandwich = models.ForeignKey(Sandwich, on_delete=models.CASCADE)
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)

    class Meta:
        db_table = 'sandwich_order'

class OrderedIngredients(models.Model):
    sandwich_order = models.ForeignKey(SandwichOrder, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)

    class Meta:
        db_table = 'ordered_ingredients'

class Status(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'status'

class SandwichStatus(models.Model):
    sandwich_order = models.ForeignKey(SandwichOrder, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    update_time = models.DateTimeField()

    class Meta:
        db_table = 'sandwich_status'

