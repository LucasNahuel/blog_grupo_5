from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import post, Comentario, Categoria
from .forms import Crear_post as Crear_post_form
from .forms import ComentarioForm
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import Colaborador_mixin, Creador_mixin
#from .mixins import ColaboradorMixin, CreadorMixin

# Create your views here.

class Lista_post(ListView):
    template_name = 'post/posts.html'
    model = post
    context_object_name = 'posts'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()

        categoria_seleccionada= self.request.GET.get('categoria')
        
        if categoria_seleccionada:
            queryset = queryset.filter(categoria=categoria_seleccionada)
         
        #Ordenar las publicaciones
        orden= self.request.GET.get('orderby') 
        if orden:
            if orden == 'fecha_asc':
                queryset =queryset.order_by('fecha')
            elif orden =='fecha_desc':
                queryset == queryset.order_by('-fecha')
            elif orden == 'alf_asc':
                queryset == queryset.order_by('titulo')   
            elif orden == 'alf_desc':
                queryset == queryset.order_by('-titulo')            
                     
        return queryset    
        
    
class Crear_post(LoginRequiredMixin, CreateView):
    template_name = 'post/crear_post.html'
    model = post
    form_class = Crear_post_form

    def form_valid(self, form):
        f = form.save(commit=False) # aca le paro el carro al formulario para que no guarde
        f.creador_id = self.request.user.id
        return super().form_valid(f)
    

    def get_success_url(self):
        return reverse('posts')


class Editar_post(LoginRequiredMixin, Creador_mixin, UpdateView):
    model = post
    template_name = 'post/editar_post.html'
    form_class = Crear_post_form
    success_url = '../'


class Eliminar_post(LoginRequiredMixin, Creador_mixin, DeleteView):
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

        if not self.request.user.is_authenticated:
            return redirect ('posts')
        
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
        
class BorrarComentarioView(LoginRequiredMixin, Creador_mixin, DeleteView):
    template_name='comentarios/borrar_comentario.html'
    model= Comentario
    
    def get_success_url(self):
        return reverse ('detalle_post', args =[self.object.publicacion.id] ) #modificar por post.id
    
class EditarComentarioView(LoginRequiredMixin, Creador_mixin, UpdateView):
    template_name= 'comentarios/editar_comentario.html'
    model= Comentario
    form_class =ComentarioForm
    
    def get_success_url(self):
        return reverse ('detalle_post', args =[self.object.publicacion.id] ) #modificar por postid
    


def Buscar_post(request):
    post_coincidentes_titulos = post.objects.filter(titulo__contains=request.GET.get('q'))

    post_coincidentes_cuerpo = post.objects.filter(cuerpo__contains=request.GET.get('q'))

    posts = post_coincidentes_titulos.union(post_coincidentes_cuerpo, all=False)

    ctx = {
        'posts' : posts
    }

    return render(request, 'post/buscar_post.html', ctx)