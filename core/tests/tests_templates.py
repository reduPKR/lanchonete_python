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

    def test_filter_ingredient_status_ok(self):
        response = self.client.get(reverse("filter_ingredient_view"))
        self.assertEqual(response.status_code, 200)

    def test_filter_ingredient(self):
        response = self.client.get(reverse("filter_ingredient_view"))
        self.assertTemplateUsed(response, "ingredient/filter.html")

    #Lanches
    def test_menu_sandwish_status_ok(self):
        response = self.client.get(reverse("menu_sandwish_view"))
        self.assertEqual(response.status_code, 200)

    def test_menu_sandwish(self):
        response = self.client.get(reverse("menu_sandwish_view"))
        self.assertTemplateUsed(response, "sandwish/menu.html")

    def test_create_sandwish_status_ok(self):
        response = self.client.get(reverse("create_sandwish_view"))
        self.assertEqual(response.status_code, 200)

    def tsandwish_ingredient(self):
        response = self.client.get(reverse("create_sandwish_view"))
        self.assertTemplateUsed(response, "sandwish/create.html")
    #
    # def test_list_sandwish_status_ok(self):
    #     response = self.client.get(reverse("list_sandwish_view"))
    #     self.assertEqual(response.status_code, 200)
    #
    # def test_list_sandwish(self):
    #     response = self.client.get(reverse("list_sandwish_view"))
    #     self.assertTemplateUsed(response, "sandwish/list.html")
    #
    # def test_filter_sandwish_status_ok(self):
    #     response = self.client.get(reverse("filter_sandwish_view"))
    #     self.assertEqual(response.status_code, 200)
    #
    # def test_filter_sandwish(self):
    #     response = self.client.get(reverse("filter_sandwish_view"))
    #     self.assertTemplateUsed(response, "sandwish/filter.html")
