from django.forms.models import BaseModelForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView,UpdateView
from .models import Usuario
from .forms import RegistrarseForm, UserLoginForm, EditarPerfilForm
from django.contrib.auth import login, views
from django.urls import reverse
from django.contrib import messages
from .mixins import Propietario_perfil
# Create your views here.

class RegistrarseView(CreateView):
    model = Usuario
    template_name = 'usuarios/registrarse.html'
    form_class =RegistrarseForm
    
    def form_valid(self, form):
        response = super().form_valid(form)
        usuario = form.save()
        login(self.request, usuario)
        return response
    
    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Registrado correctamente.", "alert alert-success alert-dismissible fade show")
        return reverse('index')


class LoginView(views.LoginView):
    model = Usuario
    template_name = 'usuarios/login.html'
    form_class = UserLoginForm

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Sesión iniciada.", "alert alert-success alert-dismissible fade show")
        return reverse('posts')
    
def mi_perfil_view(request):
    
    return render(request,'usuarios/mi-perfil.html',{})    

class EditarPerfilView(Propietario_perfil, UpdateView):
    model = Usuario
    template_name = 'usuarios/editar-perfil.html'
    form_class=EditarPerfilForm
    
    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Mensaje enviado correctamente.", "alert alert-success alert-dismissible fade show")
        return reverse('mi-perfil')
