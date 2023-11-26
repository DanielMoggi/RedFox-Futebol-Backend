from rest_framework import serializers
from RedFox.models import Partida


class PartidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partida
        fields = "__all__"
        depth = 2

