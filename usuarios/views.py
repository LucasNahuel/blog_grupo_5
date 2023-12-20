from django.shortcuts import render
from django.views.generic import CreateView,UpdateView
from .models import Usuario
from .forms import RegistrarseForm, UserLoginForm, EditarPerfilForm
from django.contrib.auth import login, views
from django.urls import reverse

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


class LoginView(views.LoginView):
    model = Usuario
    template_name = 'usuarios/login.html'
    form_class = UserLoginForm
    
def mi_perfil_view(request):
    return render(request,'usuarios/mi-perfil.html',{})    

class EditarPerfilView(UpdateView):
    model = Usuario
    template_name = 'usuarios/editar-perfil.html'
    form_class=EditarPerfilForm
    
    def get_succes_url(self):
        return reverse('mi-perfil')
