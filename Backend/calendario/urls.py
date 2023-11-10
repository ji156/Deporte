from django.urls import path
from . import views

urlpatterns = [
    path('api/calendario/laliga/', views.CalendarioLaLigaList.as_view(),
         name='calendario_laliga'),
    path('api/calendario/premierleague/', views.CalendarioPremierLeagueList.as_view(),
         name='calendario_premierleague'),
    path('api/calendario/seriea/', views.CalendarioSerieAList.as_view(),
         name='calendario_seriea'),
    path('api/calendario/bundesliga/', views.CalendarioBundesligaList.as_view(),
         name='calendario_bundesliga'),
    path('api/calendario/ligue1/', views.CalendarioLigue1List.as_view(),
         name='calendario_ligue1'),
    path('api/calendario/laligafemenina/', views.CalendarioLaLigaFemeninaList.as_view(),
         name='calendario_laliga_femenina'),
]
