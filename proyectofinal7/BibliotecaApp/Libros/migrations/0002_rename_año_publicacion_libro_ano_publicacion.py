# Generated by Django 5.0.6 on 2024-05-31 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Libros', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='libro',
            old_name='año_publicacion',
            new_name='ano_publicacion',
        ),
    ]
