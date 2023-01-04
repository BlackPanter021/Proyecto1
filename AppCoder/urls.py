from django.urls import path 
from AppCoder.views import *
from django.contrib.auth.views import LogoutView
urlpatterns = [
    #Url de inicio
    path("",inicio, name="inicio"),
    path("about/",about1, name="About"),
    path("login/",inicioSesion, name="Login"),
    path("register/",registro, name="registro"),
    path("logout/",LogoutView.as_view(template_name="AppCoder/logout.html"), name="Logout"),
    path("editar/",editarUsuario, name="EditarUsuario"),
    path("agregar2/",agregarAvatar, name="Avatar"),
    
    
    path("review/", ver_reseñas, name="reseñas"),
    path("nuevo/", agregar_reseñas, name="añadir_reseña"),
    
    path("ofertas/", ofertas1, name="ofertas_1"),
    path("ofertas1/",ver_ofertas, name="nuevas ofertas"),
    path("busquedareview/",busquedareview, name="BuscarReview"),
    path("resultados/", resultado, name="ResultadoBusqueda"),
    
    #path("lanzamientos/", agregar_lanzamientos, name="nuevos_lanzamientos"),
    #path("lanzamientoss/", ver_lanzamientos, name="ver_lanzamientos"),
    
    
    path("nuevo_lanzamientos/list",lanzamientoslist.as_view(), name="ver lanzamientos"),
    path("nuevo_lanzamientos/<int:pk>",lanzamientoDetalle.as_view(), name="Detalle lanzamientos"),
    path("nuevo_lanzamientos/nuevo",lanzamientocrear.as_view(), name="crear lanzamientos"),
    path("nuevo_lanzamientos/actualizar/<int:pk>",lanzamientoActualizar.as_view(), name="Actualizar lanzamientos"),
    path("nuevo_lanzamientos/borrar/<int:pk>",lanzamientoborrar.as_view(), name="borrar lanzamientos"),
    ]
