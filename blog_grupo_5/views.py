from django.shortcuts import render
from post import models

def index(request):

    categorias = models.Categoria.objects.all()

    ctx = {
        'comentarios' : models.Comentario.objects.order_by('id').reverse(),
        'categorias' : categorias,
        'mitad_lista' : len(categorias)/2,
        'ultimos_posts' : models.post.objects.order_by('-id')[:10]
    }

    return render(request, 'index.html', ctx)