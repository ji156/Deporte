from . import views
from django.urls import path

urlpatterns = [
    path('api/escudos/laliga', views.EscudosLaLigaList.as_view(),
         name='escudos-laliga'),
    path('api/escudos/premier', views.EscudosPremierList.as_view(),
         name='escudos-premier'),
    path('api/escudos/seriea', views.EscudosSerieaList.as_view(),
         name='escudos-seriea'),
    path('api/escudos/bundesliga', views.EscudosBundesligaList.as_view(),
         name='escudos-bundesliga'),
    path('api/escudos/ligue1', views.EscudosLigue1List.as_view(),
         name='escudos-ligue1'),
]
