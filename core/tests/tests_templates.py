from django.test import TestCase

from django.urls import reverse

class TemplatesViewTests(TestCase):

    #Home
    def test_template_home_status_ok(self):
        response = self.client.get(reverse("home_view"))
        self.assertEqual(response.status_code, 200)

    def test_template_home(self):
        response = self.client.get(reverse("home_view"))
        self.assertTemplateUsed(response, "home.html")

    #Ingredientes
    def test_menu_ingredient_status_ok(self):
        response = self.client.get(reverse("menu_ingredient_view"))
        self.assertEqual(response.status_code, 200)

    def test_menu_ingredient(self):
        response = self.client.get(reverse("menu_ingredient_view"))
        self.assertTemplateUsed(response, "ingredient/menu.html")

    def test_create_ingredient_status_ok(self):
        response = self.client.get(reverse("create_ingredient_view"))
        self.assertEqual(response.status_code, 200)

    def test_create_ingredient(self):
        response = self.client.get(reverse("create_ingredient_view"))
        self.assertTemplateUsed(response, "ingredient/create.html")

    def test_list_ingredient_status_ok(self):
        response = self.client.get(reverse("list_ingredient_view"))
        self.assertEqual(response.status_code, 200)

    def test_list_ingredient(self):
        response = self.client.get(reverse("list_ingredient_view"))
        self.assertTemplateUsed(response, "ingredient/list.html")