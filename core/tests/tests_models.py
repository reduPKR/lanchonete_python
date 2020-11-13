from django.test import TestCase
import core.dao as db

class ModelsTests(TestCase):
    def setUp(self):
        ingredient = db.Ingredient.create("Pão")
        db.Ingredient.set_value(ingredient, 1.25)
        ingredient = db.Ingredient.create("Hamburger")
        db.Ingredient.set_value(ingredient, 1)

    #Ingredientes
    def test_create_ingredient(self):
        ingredient = db.Ingredient.create("Alface")
        self.assertEqual(ingredient.id, 3)

    def test_get_ingredient_by_name(self):
        ingredient = db.Ingredient.get_by_name('Hamburger')
        self.assertEqual(ingredient.id, 2)

    def test_get_all_ingredient(self):
        ingredients = db.Ingredient.get_all()
        self.assertIsNotNone(ingredients)

    def test_filter_ingredient(self):
        ingredients = db.Ingredient.filter('Pã')
        self.assertNotEqual(len(ingredients),0)

    def test_get_ingredient_by_name(self):
        ingredient = db.Ingredient.get_by_id(1)
        self.assertEqual(ingredient.name, "Pão")

    def test_get_ingredient_update_name(self):
        db.Ingredient.update_name(2, "Bacon")
        ingredient = db.Ingredient.get_by_id(2)
        self.assertEqual(ingredient.name, "Bacon")

    def test_get_ingredient_update_price(self):
        db.Ingredient.update_price(2, 1.45)
        ingredient = db.Ingredient.get_info_by_id(2)

        ingredient.price.value = float(ingredient.price.value)
        self.assertEqual(ingredient.price.value, 1.45)

    def test_get_ingredient_update(self):
        db.Ingredient.update(2, "Bacon", 2.45)
        ingredient = db.Ingredient.get_info_by_id(2)

        ingredient.price.value = float(ingredient.price.value)
        self.assertEqual(ingredient.price.value, 2.45)


    def test_set_value_ingredient_id_1(self):
        ingredient = db.Ingredient.get_by_id(1)
        ingredient_value = db.Ingredient.set_value(ingredient, 1.50)
        self.assertEqual(ingredient_value.value, 1.5)

    def test_set_value_ingredient_id_2(self):
        ingredient = db.Ingredient.get_by_id(2)
        ingredient_value = db.Ingredient.set_value(ingredient, 1.25)
        self.assertEqual(ingredient_value.value, 1.25)

    def test_get_value_by_ingredient(self):
        ingredient = db.Ingredient.get_info_by_id(1)
        ingredient = db.Ingredient.get_value(ingredient)
        self.assertEqual(ingredient.value, 1.25)

    def test_get_value_ingredient(self):
        ingredient = db.Ingredient.get_info_by_id(1)
        self.assertEqual(ingredient.price.value, 1.25)

