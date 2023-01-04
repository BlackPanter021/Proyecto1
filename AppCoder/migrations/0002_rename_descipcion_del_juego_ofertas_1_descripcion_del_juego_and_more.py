# Generated by Django 4.1.4 on 2023-01-03 20:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AppCoder', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ofertas_1',
            old_name='Descipcion_del_juego',
            new_name='Descripcion_del_juego',
        ),
        migrations.AddField(
            model_name='nuevos_lanzamientos',
            name='Imagen',
            field=models.ImageField(null=True, upload_to='lanzamientos'),
        ),
        migrations.AddField(
            model_name='ofertas_1',
            name='Imagen',
            field=models.ImageField(null=True, upload_to='ofertas'),
        ),
        migrations.AddField(
            model_name='review',
            name='Imagen',
            field=models.ImageField(null=True, upload_to='reseña'),
        ),
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='avatares')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]