from django.db import models
from RedFox.models import Partida

class Ingresso(models.Model):
    preco = models.IntegerField(default=0)
    partida = models.ForeignKey(Partida, on_delete=models.PROTECT)
