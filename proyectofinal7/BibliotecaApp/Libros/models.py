from django.db import models
from autor.models import Autor

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    genero = models.CharField(max_length=100)
    anio_publicacion = models.IntegerField()
    numero_paginas = models.IntegerField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
