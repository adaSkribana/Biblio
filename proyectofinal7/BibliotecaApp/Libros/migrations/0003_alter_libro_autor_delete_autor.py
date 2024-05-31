# Generated by Django 5.0.6 on 2024-05-31 16:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Libros', '0002_rename_año_publicacion_libro_ano_publicacion'),
        ('autor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autor.autor'),
        ),
        migrations.DeleteModel(
            name='Autor',
        ),
    ]