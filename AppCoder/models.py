from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class review(models.Model):
    Nombre_del_videojuego = models.CharField(max_length=60)
    Fecha=models.DateField()
    Reseña= models.CharField(max_length=100)
    Calificacion=models.IntegerField()
    
class nuevos_lanzamientos(models.Model):
    Nombre_del_videojuego = models.CharField(max_length=60)
    Fecha_de_lanzamiento=models.DateField()
    
    

class ofertas_1(models.Model):
    Nombre_del_juego = models.CharField(max_length=60)
    Descripcion_del_juego = models.CharField(max_length=100)
    Ofertas=models.CharField(max_length=100)
    
    
class Avatar(models.Model):
    usuario= models.ForeignKey(User, on_delete=models.CASCADE)
    imagen= models.ImageField(upload_to="avatares", null=True,blank=True)