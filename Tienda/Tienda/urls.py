"""Tienda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import main
from Productos.views import *
from Cuentas.views import RegistroPagina, LoginPagina, UsuarioEdicion, CambioPassword, cambiosExitosos 
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name='inicio'),
    path('Productos/', busquedaProductos),
    path('ResultadosBusqueda/', buscar),
    path('AgregarProducto/', AgregarProducto.as_view()),
    path('about/', about),
    path('contacto/', contacto),
    path('listaProductos/', listaProductos),
    path('FormularioRegistro/', RegistroPagina.as_view()),
    path('FormularioLogin/', LoginPagina.as_view()),
    path('Logout/', LogoutView.as_view(template_name='logout.html')),
    path('editarPerfil/', UsuarioEdicion.as_view()),
    path('cambiarContraseña/', CambioPassword.as_view()),
    path('cambiosExitosos/', cambiosExitosos, name='cambiosExitosos'),

    path('ComputadorasLista/', ComputadorasLista.as_view(), name='computadoras'),
    path('LaptopsLista/', LaptopsLista.as_view(), name='laptops'),
    path('CelularesLista/', CelularesLista.as_view(), name='celulares'),
    path('TabletsLista/', TabletsLista.as_view(), name='tablets'),
    path('TelevisoresLista/', TelevisoresLista.as_view(), name='televisores'),

    path('ComputadoraDetalle/<int:pk>/', ComputadoraDetalle.as_view(), name='computadora'), 
    path('LaptopDetalle/<int:pk>/', LaptopsDetalle.as_view(), name='laptop'), 
    path('CelularDetalle/<int:pk>/', CelularesDetalle.as_view(), name='celular'),
    path('TabletDetalle/<int:pk>/', TabletsDetalle.as_view(), name='tablet'),
    path('TelevisorDetalle/<int:pk>/', TelevisoresDetalle.as_view(), name='televisor'), 

    path('editarComputadora/<int:pk>/', editarComputadora.as_view(), name='editarComputadora'),
    path('editarLaptop/<int:pk>/', editarLaptop.as_view(), name='editarLaptop'),
    path('editarCelular/<int:pk>/', editarCelular.as_view(), name='editarCelular'),
    path('editarTablet/<int:pk>/', editarTablet.as_view(), name='editarTablet'),
    path('editarTelesvisor/<int:pk>/', editarTelevisor.as_view(), name='editarTelevisor'),
    
    path('borrarComputadora/<int:pk>/', borrarComputadora.as_view(), name='borrarComputadora'),
    path('borrarLaptop/<int:pk>/', borrarLaptop.as_view(), name='borrarLaptop'),
    path('borrarCelular/<int:pk>/', borrarLaptop.as_view(), name='borrarCelular'),
    path('borrarTablet/<int:pk>/', borrarLaptop.as_view(), name='borrarTablet'),
    path('borrarTelevisor/<int:pk>/', borrarLaptop.as_view(), name='borrarTelevisor'),


    path('ComputadoraDetalle/<int:pk>/comentarios/', ComentarioPagina.as_view(), name='comentario'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
