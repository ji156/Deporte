from rest_framework import serializers
from .models import ClasificacionLaLiga


class ClasificacionLaLigaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClasificacionLaLiga
        fields = '__all__'
