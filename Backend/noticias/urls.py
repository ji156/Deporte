from django.urls import path
from . import views

urlpatterns = [
    path('api/noticias/', views.NoticiasList.as_view(), name='noticias-list'),
    # Otras rutas relacionadas con noticias, si las tienes.
]
