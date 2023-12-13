from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import post
from .forms import Crear_post as Crear_post_form
from .forms import ComentarioForm
from django.urls import reverse

# Create your views here.

class Lista_post(ListView):
    template_name = 'post/posts.html'
    model = post
    context_object_name = 'posts'
    
class Crear_post(CreateView):
    template_name = 'post/crear_post.html'
    model = post
    form_class = Crear_post_form

    def form_valid(self, form):
        f = form.save(commit=False) # aca le paro el carro al formulario para que no guarde
        f.creador_id = self.request.user.id
        return super().form_valid(f)
    

    def get_success_url(self):
        return reverse('crear_post')





class Editar_post(UpdateView):
    model = post
    template_name = 'post/editar_post.html'
    form_class = Crear_post_form
    success_url = '../'


class Eliminar_post(DeleteView):
    model = post
    template_name = 'post/eliminar_post.html'
    success_url = '../'


class Detalle_Post(DetailView):
    model=post
    template_name = 'post/detalle_post.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ComentarioForm()
        return context


    def post(self, request, *args, **kwargs):

        publicacion = self.get_object()
        form = ComentarioForm(request.POST)

        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.creador_id = self.request.user.id
            comentario.publicacion = publicacion
            comentario.save()
            return super().get(request)
        else:
            return super().get(request)