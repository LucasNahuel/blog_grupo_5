from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import post
from .forms import Crear_post

# Create your views here.

class Lista_post(ListView):
    template_name = 'post/posts.html'
    model = post
    context_object_name = 'posts'
    
class Crear_post(CreateView):
    template_name = 'post/crear_post.html'
    model = post
    form_class = Crear_post
