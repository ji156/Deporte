# serializers.py
from rest_framework import serializers
from .models import EscudosLaLiga
from .models import EscudosPremier
from .models import EscudosSeriea
from .models import EscudosBundesliga
from .models import EscudosLigue1


class EscudosLaLigaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EscudosLaLiga
        fields = ['id', 'nombre', 'imagen']


class EscudosPremierSerializer(serializers.ModelSerializer):
    class Meta:
        model = EscudosPremier
        fields = ['id', 'nombre', 'imagen']


class EscudosSerieaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EscudosSeriea
        fields = ['id', 'nombre', 'imagen']


class EscudosBundesligaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EscudosBundesliga
        fields = ['id', 'nombre', 'imagen']


class EscudosLigue1Serializer(serializers.ModelSerializer):
    class Meta:
        model = EscudosLigue1
        fields = ['id', 'nombre', 'imagen']
