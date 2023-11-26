from django.db import models
from uploader.models import Image

class Time(models.Model):
    nome = models.CharField(max_length=100)
    imagem = models.ForeignKey(Image, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome