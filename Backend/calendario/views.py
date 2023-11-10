from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import CalendarioLaLiga
from .models import CalendarioLaLigaFemenina
from .models import CalendarioPremierLeague
from .models import CalendarioSerieA
from .models import CalendarioBundesliga
from .models import CalendarioLigue1
from .serializers import CalendarioLaLigaSerializer
from .serializers import CalendarioPremierLeagueSerializer
from .serializers import CalendarioSerieASerializer
from .serializers import CalendarioBundesligaSerializer
from .serializers import CalendarioLigue1Serializer
from .serializers import CalendarioLaLigaFemeninaSerializer


class CalendarioLaLigaList(generics.ListCreateAPIView):
    queryset = CalendarioLaLiga.objects.all()
    serializer_class = CalendarioLaLigaSerializer


class CalendarioLaLigaFemeninaList(generics.ListCreateAPIView):
    queryset = CalendarioLaLigaFemenina.objects.all()
    serializer_class = CalendarioLaLigaFemeninaSerializer


class CalendarioPremierLeagueList(generics.ListCreateAPIView):
    queryset = CalendarioPremierLeague.objects.all()
    serializer_class = CalendarioPremierLeagueSerializer


class CalendarioSerieAList(generics.ListCreateAPIView):
    queryset = CalendarioSerieA.objects.all()
    serializer_class = CalendarioSerieASerializer


class CalendarioBundesligaList(generics.ListCreateAPIView):
    queryset = CalendarioBundesliga.objects.all()
    serializer_class = CalendarioBundesligaSerializer


class CalendarioLigue1List(generics.ListCreateAPIView):
    queryset = CalendarioLigue1.objects.all()
    serializer_class = CalendarioLigue1Serializer
