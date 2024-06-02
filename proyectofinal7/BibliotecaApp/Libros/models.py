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

    def get_all_fields(self):
        return {
            'titulo': self.titulo,
            'genero': self.genero,
            'anio_publicacion': self.anio_publicacion,
            'numero_paginas': self.numero_paginas,
            'autor': self.autor.nombre,  # Asegúrate de que el modelo Autor tenga un campo 'nombre'
            'autor': self.autor.nacionalidad
        }
