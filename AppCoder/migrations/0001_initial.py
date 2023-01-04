# Generated by Django 4.1.4 on 2022-12-31 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='nuevos_lanzamientos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre_del_videojuego', models.CharField(max_length=60)),
                ('Fecha_de_lanzamiento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ofertas_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre_del_juego', models.CharField(max_length=60)),
                ('Descipcion_del_juego', models.CharField(max_length=100)),
                ('Ofertas', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre_del_videojuego', models.CharField(max_length=60)),
                ('Fecha', models.DateField()),
                ('Reseña', models.CharField(max_length=100)),
                ('Calificacion', models.IntegerField()),
            ],
        ),
    ]
