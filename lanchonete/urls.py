from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView

from core.pages.templates import views as template
from core.pages.ingredient import views as ingredient
from core.pages.sandwich import views as sandwich

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', RedirectView.as_view(url='/home/')),
    path('home/', template.home, name='home_view'),

    path('ingredient/menu/', ingredient.menu, name='menu_ingredient_view'),
    path('ingredient/create/', ingredient.create, name='create_ingredient_view'),
    path('ingredient/create/submit', ingredient.create_submit),
    path('ingredient/list/', ingredient.list, name='list_ingredient_view'),
    path('ingredient/filter/', ingredient.filter, name='filter_ingredient_view'),
    path('ingredient/filter/submit', ingredient.filter_submit),
    path('ingredient/edit/<int:id>', ingredient.edit),
    path('ingredient/edit/submit', ingredient.edit_submit),

    path('sandwich/menu/', sandwich.menu, name='menu_sandwich_view'),
    path('sandwich/create/', sandwich.create, name='create_sandwich_view'),
    path('sandwich/create/submit', sandwich.create_submit),
    path('sandwich/list', sandwich.list, name='list_sandwich_view'),
    path('sandwich/edit/<int:id>', sandwich.edit),
    path('sandwich/edit/submit', sandwich.edit_submit),
]
