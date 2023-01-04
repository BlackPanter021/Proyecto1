from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import *
from AppCoder.forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import  AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.


def inicioSesion(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contra  = form.cleaned_data.get("password")
            
            user = authenticate(username= usuario,password= contra)
            if user:
                login(request, user)
                return render(request, "AppCoder/inicio.html", {'mensaje':f"Bienvenido al 8x  {user}"})
        else:
            return render(request, "AppCoder/inicio.html", {'mensaje':"Datos incorrectos."})

    else:
        form = AuthenticationForm()
    return render(request,"AppCoder/login.html",{"formulario2":form})


def registro(request):
    if request.method == "POST":
        form= UsuarioRegistro(request.POST)
        if form.is_valid():
            username= form.cleaned_data["username"]
            form.save()
            return render(request, "AppCoder/inicio.html",{"mensaje":"Usuario creado."})
    else:
        form=UsuarioRegistro()
    return render(request,"AppCoder/registro.html",{"formulario2":form} )

def editarUsuario(request):
    usuario =request.user
    if request.method == "POST":
        form= Formularioeditar(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            
            usuario.email= info["email"]
            usuario.set.password(info["password"])
            usuario.first_name= info["forst_name"]
            usuario.last_name= info["last_name"]
            
            usuario.save()
            
            return render(request, "AppCoder/inicio.html")
    else:
        form=Formularioeditar(initial={
            "email":usuario.email,
            "first_name":usuario.first_name,
            "last_name":usuario.last_name,
        })
            
    return render(request, "AppCoder/editarperfil.html",{"formulario2":form, "usaurio":usuario})

@login_required
def agregarAvatar(request):
    if request.method=="POST":
        form=Avatarformulario(request.POST, request.FILES)
        
        if form.is_valid():
            usuarioActual= User.objects.get(username=request.user)
            avatar= Avatar(usuario=usuarioActual, imagen=form.cleaned_data["imagen"])
            avatar.save()
            return render(request, "AppCoder/inicio.html")
        
    else:
        form=Avatarformulario()
    return render(request, "AppCoder/agregarAvatar.html", {"formulario2":form})

def inicio(request):
    
    return render(request,"AppCoder/inicio.html")


def about1(request):
    return render(request,"AppCoder/about.html")

# Vistas de reseñas 
def agregar_reseñas(request):
    if request.method == "POST":
        miformulario=reviewformulario(request.POST)
        if miformulario.is_valid():
            info = miformulario.cleaned_data
            
            lreview=review(Nombre_del_videojuego=info ["Nombre_del_videojuego"],Fecha=info ["Fecha"],Reseña=info ["Reseña"],Calificacion=info ["Calificacion"])
            lreview.save()
            
            return render(request,"AppCoder/inicio.html")
            
    else:
        miformulario=reviewformulario()
            
    return render(request,"AppCoder/agregar_reseñas.html", {"formu1": miformulario})

@login_required
def ver_reseñas(request):
    
    allreseñas = review.objects.all()
    
    return render(request,"AppCoder/ver_reseñas.html", {"reseñas":allreseñas})

def busquedareview(request):
    return render(request, "AppCoder/inicio.html")


def resultado(request):    
        if request.GET["nombre"]:
            nombre = request.GET["nombre"]
            reseña= review.objects.filter(nombre_iexact=nombre)
            return render(request,"AppCoder/inicio.html",{"reseña":reseña, "nombre":nombre})
        
        else:
            respuesta="No enviaste ningun dato."
        
        return HttpResponse(respuesta)
    

#Vistas de ofertas 

def ver_ofertas(request):
    allofertas = ofertas_1.objects.all()
    
    return render(request,"AppCoder/ver_ofertas.html", {"oferta":allofertas})


def ofertas1(request):
    
    if request.method == "POST":
        miformulario3=ofertasformulario(request.POST)
        if miformulario3.is_valid():
            info = miformulario3.cleaned_data
            
            ofertas2=ofertas_1(Nombre_del_juego=info ["Nombre_del_juego"],Descripcion_del_juego=info ["Descripcion_del_juego"],Ofertas=info["Ofertas"])
            ofertas2.save()
            
            return render(request,"AppCoder/inicio.html")
            
    else:
        miformulario3=ofertasformulario()
    return render(request,"AppCoder/agregar_ofertas.html", {"formu3": miformulario3})





class lanzamientoslist(LoginRequiredMixin, ListView):
    model=nuevos_lanzamientos
    template_name="AppCoder/nuevos_lanzamientos_list.html"

class lanzamientoDetalle(LoginRequiredMixin,DetailView):
    model=nuevos_lanzamientos
    template_name="AppCoder/nuevos_lanzamientos_detalle.html"
    
class lanzamientocrear(LoginRequiredMixin,CreateView):
    model=nuevos_lanzamientos
    success_url="/AppCoder/nuevo_lanzamientos/list"
    fields= ["Nombre_del_videojuego","Fecha_de_lanzamiento"]
    
class lanzamientoActualizar(LoginRequiredMixin,UpdateView):
    model=nuevos_lanzamientos
    success_url="/AppCoder/nuevo_lanzamientos/list"
    fields=["Nombre_del_videojuego","Fecha_de_lanzamiento"]
    
class lanzamientoborrar(LoginRequiredMixin,DeleteView):
    model=nuevos_lanzamientos
    success_url="/AppCoder/nuevo_lanzamientos/list"