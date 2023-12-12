from django.shortcuts import render
from django.views.generic import CreateView
from .models import Usuario
from .forms import RegistrarseForm, UserLoginForm
from django.contrib.auth import login, views

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