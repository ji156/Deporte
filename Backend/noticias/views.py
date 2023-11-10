from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Noticias
from .serializers import NoticiasSerializer


# esto es una vista basada en clase
class NoticiasList(generics.ListCreateAPIView):
    queryset = Noticias.objects.all()
    serializer_class = NoticiasSerializer
