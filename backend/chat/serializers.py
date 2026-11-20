from rest_framework import serializers

from .models import Canal, Mensaje


class CanalSerializer(serializers.ModelSerializer):
    creador = serializers.CharField(source='creador.username', read_only=True)

    class Meta:
        model = Canal
        fields = ['id', 'nombre', 'descripcion', 'creador', 'creado']


class MensajeSerializer(serializers.ModelSerializer):
    autor = serializers.CharField(source='autor.username', read_only=True)

    class Meta:
        model = Mensaje
        fields = ['id', 'canal', 'autor', 'texto', 'creado', 'editado']
        read_only_fields = ['editado']
