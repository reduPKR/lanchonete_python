from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView

from core.pages.templates import views as template
from core.pages.ingredient import views as ingredient

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', RedirectView.as_view(url='/home/')),
    path('home/', template.home, name='home_view'),

    path('ingredient/menu/', ingredient.menu, name='menu_ingredient_view'),
    path('ingredient/create/', ingredient.create, name='create_ingredient_view'),
    path('ingredient/create/submit', ingredient.create_submit),
    path('ingredient/list', ingredient.list, name='list_ingredient_view'),
]
