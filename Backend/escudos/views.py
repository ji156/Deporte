from django.shortcuts import render

# views.py
from rest_framework import generics
# LaLiga
from .models import EscudosLaLiga
from .serializers import EscudosLaLigaSerializer
# Premier
from .models import EscudosPremier
from .serializers import EscudosPremierSerializer
# Seriea
from .models import EscudosSeriea
from .serializers import EscudosSerieaSerializer
# Bundesliga
from .models import EscudosBundesliga
from .serializers import EscudosBundesligaSerializer
# Ligue1
from .models import EscudosLigue1
from .serializers import EscudosLigue1Serializer


class EscudosLaLigaList(generics.ListCreateAPIView):
    queryset = EscudosLaLiga.objects.all()
    serializer_class = EscudosLaLigaSerializer


class EscudosPremierList(generics.ListCreateAPIView):
    queryset = EscudosPremier.objects.all()
    serializer_class = EscudosPremierSerializer


class EscudosSerieaList(generics.ListCreateAPIView):
    queryset = EscudosSeriea.objects.all()
    serializer_class = EscudosSerieaSerializer


class EscudosBundesligaList(generics.ListCreateAPIView):
    queryset = EscudosBundesliga.objects.all()
    serializer_class = EscudosBundesligaSerializer


class EscudosLigue1List(generics.ListCreateAPIView):
    queryset = EscudosLigue1.objects.all()
    serializer_class = EscudosLigue1Serializer
