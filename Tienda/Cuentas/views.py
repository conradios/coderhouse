from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView 
from django.contrib.auth import login
from .forms import FormularioRegistroUsuario, FormularioEdicion, FormularioCambioPassword

# Create your views here.

class LoginPagina(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_autheticated_user = True
    success_url = reverse_lazy('inicio')

    def get_success_url(self):
        return reverse_lazy('inicio')

class RegistroPagina(FormView):
    template_name = 'registro.html'
    form_class = FormularioRegistroUsuario
    redirect_autheticated_user = True
    success_url = reverse_lazy('inicio')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegistroPagina, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('inicio')
        return super(RegistroPagina, self).get(*args, **kwargs)
    
class UsuarioEdicion(UpdateView):
    form_class = FormularioEdicion
    template_name= 'editarPerfil.html'
    success_url = reverse_lazy('cambiosExitosos')

    def get_object(self):
        return self.request.user
    
class CambioPassword(PasswordChangeView):
    form_class = FormularioCambioPassword
    template_name = 'cambiarContraseña.html'
    success_url = reverse_lazy('cambiosExitosos')

def cambiosExitosos(request):
    return render(request, 'cambiosExitosos.html', {})