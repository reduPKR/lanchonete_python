from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView

from core.pages.templates import views as template
from core.pages.ingredient import views as ingredient
from core.pages.sandwich import views as sandwich
from core.pages.beverage import views as beverage
from core.pages.purchase import views as purchase

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
    path('sandwich/remove/<int:sandwich_id>/<int:ingredient_id>', sandwich.remove_ingredient),
    path('sandwich/filter/', sandwich.filter, name='filter_sandwich_view'),
    path('sandwich/filter/submit', sandwich.filter_submit),

    path('beverage/menu/', beverage.menu, name='menu_beverage_view'),
    path('beverage/create/', beverage.create, name='create_beverage_view'),
    path('beverage/create/submit', beverage.create_submit),
    path('beverage/list', beverage.list, name='list_beverage_view'),
    path('beverage/filter/', beverage.filter, name='filter_beverage_view'),
    path('beverage/filter/submit', beverage.filter_submit),
    path('beverage/edit/<int:id>', beverage.edit),
    path('beverage/edit/submit', beverage.edit_submit),

    path('purchase/menu/', purchase.menu),
    path('purchase/create/', purchase.create),
    path('purchase/create/submit', purchase.create_submit),
    path('purchase/list', purchase.list),
    path('purchase/close/<int:id>', purchase.close),
]