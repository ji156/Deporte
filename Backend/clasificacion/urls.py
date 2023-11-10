from django.urls import path
from . import views

urlpatterns = [
    path('api/clasificacion/', views.ClasificacionLaLigaList.as_view(),
         name='clasificacion-list'),
]
