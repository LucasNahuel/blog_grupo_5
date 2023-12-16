from django.db import models
from django.urls import reverse
from usuarios.models import Usuario


# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class post(models.Model):
    fecha = models.DateField(auto_now_add=True)
    titulo = models.CharField(max_length=50)
    cuerpo = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, related_name='posts', null=True)
    creador = models.ForeignKey(Usuario, related_name='posts', on_delete=models.CASCADE)
    imagen =models.ImageField(upload_to='imagenes_post', null=True, blank=True)

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('posts')
    

class Comentario(models.Model):
    fecha = models.DateField(auto_now_add=True)
    texto = models.TextField()
    publicacion = models.ForeignKey(post, on_delete=models.CASCADE, related_name='comentarios') #modificar por post.id
    creador = models.ForeignKey(Usuario, related_name='comentarios', on_delete=models.CASCADE)

    def __str__(self):
        return self.publicacion.titulo + "-" + self.creador.username