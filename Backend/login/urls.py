# urls.py

from django.urls import path
from .views import guardar_registro

urlpatterns = [
    path('guardar-registro/', guardar_registro, name='guardar-registro'),
    # Otros patrones de URL de tu aplicación
]
