from rest_framework.viewsets import ModelViewSet

from RedFox.models import Ingresso
from RedFox.serializers import IngressoSerializer


class IngressoViewSet(ModelViewSet):
    queryset = Ingresso.objects.all()
    serializer_class = IngressoSerializer