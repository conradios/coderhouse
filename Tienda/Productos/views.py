from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Productos, Comentario
from .forms import FormularioNuevoProducto, ActualizarProducto, FormComentario
from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView


# Create your views here.

def resultadosBusqueda(request):
    return render(request, "resultadosBusqueda.html")

def busquedaProductos(request):

    return render(request, "busqueda.html")

def about(request):

    return render(request, 'about.html')

def contacto(request):
    
    return render(request, 'contacto.html')

def buscar(request):

    if request.GET["prod"]:

        #mensaje="Buscaste: %r" %request.GET["prod"]
        producto=request.GET["prod"]

        articulos = Productos.objects.filter(nombre__icontains=producto)

        return render(request, "resultadosBusqueda.html", {"articulos": articulos, "query":producto})

    else:

        mensaje="No introduciste un producto valido"

    return HttpResponse(mensaje)

def listaProductos(request):
    
    todosProductos = Productos.objects.all()
    
    context = {
       'productos': todosProductos
     }

    return render(request, 'listaProductos.html', context)


class AgregarProducto(LoginRequiredMixin, CreateView):
    model = Productos
    form_class = FormularioNuevoProducto
    success_url = reverse_lazy('inicio')
    template_name = 'agregarProducto.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AgregarProducto, self).form_valid(form)
    
# LISTAS

class ComputadorasLista(LoginRequiredMixin, ListView):
    context_object_name = 'computadoras'
    queryset = Productos.objects.filter(producto__startswith='computadora')
    template_name = 'ComputadorasLista.html'
    login_url = '/FormularioLogin/'

class LaptopsLista(LoginRequiredMixin, ListView):
    context_object_name = 'laptops'
    queryset = Productos.objects.filter(producto__startswith='laptop')
    template_name = 'LaptopsLista.html'
    login_url = '/FormularioLogin/'

class CelularesLista(LoginRequiredMixin, ListView):
    context_object_name = 'celulares'
    queryset = Productos.objects.filter(producto__startswith='celular')
    template_name = 'CelularesLista.html'
    login_url = '/FormularioLogin/'

class TabletsLista(LoginRequiredMixin, ListView):
    context_object_name = 'tablets'
    queryset = Productos.objects.filter(producto__startswith='tablet')
    template_name = 'TabletsLista.html'
    login_url = '/FormularioLogin/'

class TelevisoresLista(LoginRequiredMixin, ListView):
    context_object_name = 'televisores'
    queryset = Productos.objects.filter(producto__startswith='televisor')
    template_name = 'TelevisoresLista.html'
    login_url = '/FormularioLogin/'

# DETALLES

class ComputadoraDetalle(LoginRequiredMixin, DetailView):
    model = Productos
    context_object_name = 'computadora'
    template_name = 'computadoraDetalle.html'

class LaptopsDetalle(LoginRequiredMixin, DetailView):
    model = Productos
    context_object_name = 'laptop'
    template_name = 'laptopDetalle.html'

class CelularesDetalle(LoginRequiredMixin, DetailView):
    model = Productos
    context_object_name = 'celular'
    template_name = 'celularesDetalle.html'

class TabletsDetalle(LoginRequiredMixin, DetailView):
    model = Productos
    context_object_name = 'tablet'
    template_name = 'tabletDetalle.html'

class TelevisoresDetalle(LoginRequiredMixin, DetailView):
    model = Productos
    context_object_name = 'televisor'
    template_name = 'televisorDetalle.html'

# EDICION

class editarComputadora(LoginRequiredMixin, UpdateView):
    model = Productos
    form_class = ActualizarProducto
    success_url = reverse_lazy('inicio')
    context_object_name = 'computadora'
    template_name = 'editarComputadora.html'

class editarLaptop(LoginRequiredMixin, UpdateView):
    model = Productos
    form_class = ActualizarProducto
    success_url = reverse_lazy('inicio')
    context_object_name = 'laptop'
    template_name = 'editarLaptop.html'

class editarCelular(LoginRequiredMixin, UpdateView):
    model = Productos
    form_class = ActualizarProducto
    success_url = reverse_lazy('inicio')
    context_object_name = 'celular'
    template_name = 'editarCelular.html'

class editarTablet(LoginRequiredMixin, UpdateView):
    model = Productos
    form_class = ActualizarProducto
    success_url = reverse_lazy('inicio')
    context_object_name = 'tablet'
    template_name = 'editarTablet.html'

class editarTelevisor(LoginRequiredMixin, UpdateView):
    model = Productos
    form_class = ActualizarProducto
    success_url = reverse_lazy('inicio')
    context_object_name = 'televisor'
    template_name = 'editarTelevisor.html'

# BORRAR

class borrarComputadora(LoginRequiredMixin, DeleteView):
    model = Productos
    success_url = reverse_lazy('computadoras')
    context_object_name = 'computadora'
    template_name = 'borrarComputadora.html'

class borrarLaptop(LoginRequiredMixin, DeleteView):
    model = Productos
    success_url = reverse_lazy('laptops')
    context_object_name = 'laptop'
    template_name = 'borrarLaptop.html'

class borrarCelular(LoginRequiredMixin, DeleteView):
    model = Productos
    success_url = reverse_lazy('celulares')
    context_object_name = 'celular'
    template_name = 'borrarCelular.html'

class borrarTablet(LoginRequiredMixin, DeleteView):
    model = Productos
    success_url = reverse_lazy('tablets')
    context_object_name = 'tablet'
    template_name = 'borrarTablet.html'

class borrarTelevisor(LoginRequiredMixin, DeleteView):
    model = Productos
    success_url = reverse_lazy('televisores')
    context_object_name = 'televisor'
    template_name = 'borrarTelevisor.html'

# COMENTARIOS

class ComentarioPagina(LoginRequiredMixin, CreateView):
    model = Comentario
    form_class = FormComentario
    template_name = 'comentarios.html'
    success_url = reverse_lazy('inicio')

    def form_valid(self, form):
        form.instance.comentario_id = self.kwargs['pk']
        return super(ComentarioPagina, self).form_valid(form)
    
