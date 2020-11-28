from django.test import TestCase
from core.dao import Ingredient, Sandwich, Beverage

class ModelsTests(TestCase):
    def setUp(self):
        ingredient = Ingredient.create("Pão")
        Ingredient.set_value(ingredient, 1.25)
        ingredient = Ingredient.create("Hamburger")
        Ingredient.set_value(ingredient, 1)
        ingredient = Ingredient.create("Bacon")
        Ingredient.set_value(ingredient, 2)

        name = "X-Bacon"
        list = ["Pão", "Hamburger", "Bacon"]
        profit = 5.5
        sandwich = Sandwich.create(name, profit, list)

        beverage = Beverage.create("Coca-cola", "2 Litros", 6)


    #Ingredientes
    def test_create_ingredient(self):
        ingredient = Ingredient.create("Alface")
        self.assertEqual(ingredient.id, 4)

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
        self.assertEqual(ingredients[0].price.value, 2)
        self.assertEqual(ingredients[1].price.value, 1)

    #Sandwich
    def test_create_sandwich(self):
        name = "X-burger"
        list = ["Pão","Hamburger"]
        profit = 5.5
        sandwich = Sandwich.create(name, profit, list)
        self.assertEqual(sandwich.id, 2)

    def test_get_all_sandwich(self):
        sandwich = Sandwich.get_all()
        self.assertIsNotNone(sandwich)

    def test_get_sandwich_by_id(self):
        sandwich = Sandwich.get_by_id(1)
        self.assertIsNotNone(sandwich)

    def test_get_sandwich_update_name(self):
        Sandwich.update_name(1, "X bacon")
        sandwich = Sandwich.get_by_id(1)

        self.assertEqual(sandwich.name, "X bacon")

    def test_get_sandwich_add_profit(self):
        sandwich = Sandwich.get_by_id(1)
        Sandwich.add_profit(sandwich, 3.5)
        profit = Sandwich.get_profit(sandwich)

        self.assertEqual(profit.percent, 3.5)

    def test_get_sandwich_update(self):
        list = ["bacon"]
        Sandwich.update(1, "X-bacon", 10, list)
        sandwich = Sandwich.get_by_id(1)

        self.assertEqual(sandwich.name, "X-bacon")

    def test_get_sandwich_remove_ingredient(self):
        sandwich = Sandwich.get_by_id(1)

        Sandwich.remove_ingredient(1, 2)
        ingredients = Sandwich.sandwich_ingredients(sandwich)

        self.assertEqual(len(ingredients), 2)

    def test_filter_sandwich_name(self):
        sandwich = Sandwich.filter("X")
        self.assertNotEqual(len(sandwich), 0)

    def test_filter_sandwich_ingredient(self):
        sandwich = Sandwich.filter("Hamburger")
        self.assertNotEqual(len(sandwich), 0)

    #Beverage
    def test_create_beverage(self):
        beverage = Beverage.create("Suco de laranja", "1 Litro", 3.9)
        self.assertEqual(beverage.id, 2)

    def test_get_all_beverage(self):
        beverage = Beverage.get_all()
        self.assertIsNotNone(beverage)

    def test_filter_beverage_name(self):
        beverages = Beverage.filter("Coca-cola")
        self.assertNotEqual(len(beverages), 0)

    def test_get_beverage_by_id(self):
        beverage = Beverage.get_by_id(1)
        self.assertEqual(beverage.name,"Coca-cola")

    def test_get_beverage_update_name(self):
        Beverage.update_name(1, "Suco de laranja")
        beverage = Beverage.get_by_id(1)

        self.assertEqual(beverage.name, "Suco de laranja")

    def test_get_beverage_update(self):
        Beverage.update(1, "Suco de limão", 5)
        beverage = Beverage.get_by_id(1)

        self.assertEqual(beverage.name, "Suco de limão")