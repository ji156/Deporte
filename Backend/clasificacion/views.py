from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import ClasificacionLaLiga
from .serializers import ClasificacionLaLigaSerializer


# esto es una vista basada en clase
class ClasificacionLaLigaList(generics.ListCreateAPIView):
    queryset = ClasificacionLaLiga.objects.all()
    serializer_class = ClasificacionLaLigaSerializer
