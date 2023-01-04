from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from AppCoder.models import Avatar



class reviewformulario(forms.Form):
    
    Nombre_del_videojuego=forms.CharField()
    Fecha=forms.DateField()
    Reseña=forms.CharField()
    Calificacion=forms.IntegerField()
    
    
class lanzamientosformulario(forms.Form):
    Nombre_del_videojuego = forms.CharField()
    Fecha_de_lanzamiento=forms.DateField()
    
    
class ofertasformulario(forms.Form):
    Nombre_del_juego = forms.CharField()
    Descripcion_del_juego= forms.CharField()
    Ofertas=forms.CharField()
    
    
class UsuarioRegistro(UserCreationForm):
    email= forms.EmailField()
    password1=forms.CharField(label= "Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label= "RepetirContraseña", widget=forms.PasswordInput)
    
    class Meta:
        model= User
        fields= ["username", "email", "first_name", "last_name", "password1", "password2"]
        
        
class Formularioeditar(UserCreationForm):
    email= forms.EmailField()
    password1=forms.CharField(label= "Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label= "RepetirContraseña", widget=forms.PasswordInput)
    
    class Meta:
        model= User
        fields= ["email", "first_name", "last_name", "password1", "password2"]
        
        

class Avatarformulario(forms.ModelForm):
    
    class Meta:
        model=Avatar
        fields=["imagen"]