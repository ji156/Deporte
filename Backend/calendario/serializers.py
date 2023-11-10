from rest_framework import serializers
from .models import CalendarioLaLiga
from .models import CalendarioLaLigaFemenina
from .models import CalendarioPremierLeague
from .models import CalendarioSerieA
from .models import CalendarioBundesliga
from .models import CalendarioLigue1


class CalendarioLaLigaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalendarioLaLiga
        fields = '__all__'


class CalendarioLaLigaFemeninaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalendarioLaLigaFemenina
        fields = '__all__'


class CalendarioPremierLeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalendarioPremierLeague
        fields = '__all__'


class CalendarioSerieASerializer(serializers.ModelSerializer):
    class Meta:
        model = CalendarioSerieA
        fields = '__all__'


class CalendarioBundesligaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalendarioBundesliga
        fields = '__all__'


class CalendarioLigue1Serializer(serializers.ModelSerializer):
    class Meta:
        model = CalendarioLigue1
        fields = '__all__'
