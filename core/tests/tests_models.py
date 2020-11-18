from django.test import TestCase
from core.dao import Ingredient, Sandwich

class ModelsTests(TestCase):
    def setUp(self):
        ingredient = Ingredient.create("Pão")
        Ingredient.set_value(ingredient, 1.25)
        ingredient = Ingredient.create("Hamburger")
        Ingredient.set_value(ingredient, 1)

    #Ingredientes
    def test_create_ingredient(self):
        ingredient = Ingredient.create("Alface")
        self.assertEqual(ingredient.id, 3)

    def test_get_ingredient_by_name(self):
        ingredient = Ingredient.get_by_name('Hamburger')
        self.assertEqual(ingredient.id, 2)

    def test_get_all_ingredient(self):
        ingredients = Ingredient.get_all()
        self.assertIsNotNone(ingredients)

    def test_filter_ingredient(self):
        ingredients = Ingredient.filter('Pã')
        self.assertNotEqual(len(ingredients),0)

    def test_get_ingredient_by_id(self):
        ingredient = Ingredient.get_by_id(1)
        self.assertEqual(ingredient.name, "Pão")

    def test_get_ingredient_update_name(self):
        Ingredient.update_name(2, "Bacon")
        ingredient = Ingredient.get_by_id(2)
        self.assertEqual(ingredient.name, "Bacon")

    def test_get_ingredient_update_price(self):
        Ingredient.update_price(2, 1.45)
        ingredient = Ingredient.get_info_by_id(2)

        ingredient.price.value = float(ingredient.price.value)
        self.assertEqual(ingredient.price.value, 1.45)

    def test_get_ingredient_update(self):
        Ingredient.update(2, "Bacon", 2.45)
        ingredient = Ingredient.get_info_by_id(2)

        ingredient.price.value = float(ingredient.price.value)
        self.assertEqual(ingredient.price.value, 2.45)

    def test_set_value_ingredient_id_1(self):
        ingredient = Ingredient.get_by_id(1)
        ingredient_value = Ingredient.set_value(ingredient, 1.50)
        self.assertEqual(ingredient_value.value, 1.5)

    def test_set_value_ingredient_id_2(self):
        ingredient = Ingredient.get_by_id(2)
        ingredient_value = Ingredient.set_value(ingredient, 1.25)
        self.assertEqual(ingredient_value.value, 1.25)

    def test_get_value_by_ingredient(self):
        ingredient = Ingredient.get_info_by_id(1)
        ingredient = Ingredient.get_value(ingredient)
        self.assertEqual(ingredient.value, 1.25)

    def test_get_value_ingredient(self):
        ingredient = Ingredient.get_info_by_id(1)
        self.assertEqual(ingredient.price.value, 1.25)

    def test_get_value_ingredient_all(self):
        ingredients = Ingredient.get_all_with_price()
        self.assertEqual(ingredients[0].price.value, 1)
        self.assertEqual(ingredients[1].price.value, 1.25)

    #Sandwich
    def test_create_sandwich(self):
        name = "X-burger"
        list = ["Pão","Hamburger"]
        profit = 5.5
        sandwich = Sandwich.create(name, profit, list)
        self.assertEqual(sandwich.id, 1)

    def test_get_all_sandwich(self):
        sandwich = Sandwich.get_all()
        self.assertIsNotNone(sandwich)