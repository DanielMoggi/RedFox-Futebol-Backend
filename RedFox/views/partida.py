from rest_framework.viewsets import ModelViewSet

from RedFox.models import Partida
from RedFox.serializers import PartidaSerializer


class PartidaViewSet(ModelViewSet):
    queryset = Partida.objects.all()
    serializer_class = PartidaSerializer