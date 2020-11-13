from django.test import TestCase
import core.dao as db

class ModelsTests(TestCase):
    def setUp(self):
        db.Ingredient.create("Pão")
        db.Ingredient.create("Hamburger")

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