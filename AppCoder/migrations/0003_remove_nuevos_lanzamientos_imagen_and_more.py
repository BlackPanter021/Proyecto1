# Generated by Django 4.1.4 on 2023-01-04 01:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0002_rename_descipcion_del_juego_ofertas_1_descripcion_del_juego_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nuevos_lanzamientos',
            name='Imagen',
        ),
        migrations.RemoveField(
            model_name='ofertas_1',
            name='Imagen',
        ),
        migrations.RemoveField(
            model_name='review',
            name='Imagen',
        ),
    ]
