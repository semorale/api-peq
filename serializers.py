from django.contrib.auth.models import User
from equipos.models import Equipo
from mediciones.models import Medicion
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')

class EquipoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Equipo
		fields = ('nombre','descripcion','categoria')

class MedicionesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Medicion
		fields = ("indicador","timestamp","valor")


