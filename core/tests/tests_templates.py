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
    def test_menu_sandwich_status_ok(self):
        response = self.client.get(reverse("menu_sandwich_view"))
        self.assertEqual(response.status_code, 200)

    def test_menu_sandwich(self):
        response = self.client.get(reverse("menu_sandwich_view"))
        self.assertTemplateUsed(response, "sandwich/menu.html")

    def test_create_sandwich_status_ok(self):
        response = self.client.get(reverse("create_sandwich_view"))
        self.assertEqual(response.status_code, 200)

    def test_sandwich_create(self):
        response = self.client.get(reverse("create_sandwich_view"))
        self.assertTemplateUsed(response, "sandwich/create.html")

    def test_list_sandwich_status_ok(self):
        response = self.client.get(reverse("list_sandwich_view"))
        self.assertEqual(response.status_code, 200)

    def test_list_sandwich(self):
        response = self.client.get(reverse("list_sandwich_view"))
        self.assertTemplateUsed(response, "sandwich/list.html")

    # def test_filter_sandwich_status_ok(self):
    #     response = self.client.get(reverse("filter_sandwich_view"))
    #     self.assertEqual(response.status_code, 200)
    #
    # def test_filter_sandwich(self):
    #     response = self.client.get(reverse("filter_sandwich_view"))
    #     self.assertTemplateUsed(response, "sandwich/filter.html")
