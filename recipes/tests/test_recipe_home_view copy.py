from django.test import TestCase
from django.urls import resolve, reverse

from recipes import views

class RecipeDetailViewTest(TestCase):
    def test_recipe_detail_view_function_is_correct(self):
        view = resolve(reverse('recipes:recipes', kwargs={'pk': 1}))
        self.assertIs(view.func.view_class, views.RecipesView)

    def test_recipe_detail_view_returns_status_code_200_OK(self):
        response = self.client.get(reverse('recipes:recipes', kwargs={'pk': 1} ))
        self.assertEqual(response.status_code, 200)

    def test_recipe_detail_view_loads_correct_template(self):
        response = self.client.get(reverse('recipes:recipes',kwargs={'pk': 1}))
        self.assertTemplateUsed(response, 'recipes/pages/recipe-view.html')