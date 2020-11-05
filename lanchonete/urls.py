from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView

from core.pages.templates import views as template

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', RedirectView.as_view(url='/home/')),
    path('home/', template.home, name='home_view'),
]
