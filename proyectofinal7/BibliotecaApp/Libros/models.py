from django.db import models
from autor.models import Autor

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    genero = models.CharField(max_length=100)
    ano_publicacion = models.IntegerField()

    def __str__(self):
        return self.titulo
