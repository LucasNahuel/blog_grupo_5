from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import post
from .forms import Crear_post as Crear_post_form

# Create your views here.

class Lista_post(ListView):
    template_name = 'post/posts.html'
    model = post
    context_object_name = 'posts'
    
class Crear_post(CreateView):
    template_name = 'post/crear_post.html'
    model = post
    form_class = Crear_post_form

class Editar_post(UpdateView):
    model = post
    template_name = 'post/editar_post.html'
    form_class = Crear_post_form
    success_url = '../'


class Eliminar_post(DeleteView):
    model = post
    template_name = 'post/eliminar_post.html'
    success_url = '../'