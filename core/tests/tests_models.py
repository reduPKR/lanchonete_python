from django.test import TestCase
import core.dao.Ingredient as db

class ModelsTests(TestCase):
    def setUp(self):
        db.create("Pão")
        db.create("Hamburger")

    #Ingredientes
    def test_create_ingredient(self):
        ingredient = db.create("Alface")
        self.assertEqual(ingredient.id, 3)