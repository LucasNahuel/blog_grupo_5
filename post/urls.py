from .views import Lista_post, Crear_post, Editar_post, Eliminar_post, Detalle_Post
from django.urls import path


urlpatterns = [
    path('', Lista_post.as_view(), name='posts'),
    path('crear/', Crear_post.as_view(), name="crear_post"),
    path('editar/<int:pk>', Editar_post.as_view(), name="editar_post"),
    path('eliminar/<int:pk>', Eliminar_post.as_view(), name="eliminar_post"),
    path('detalle/<int:pk>', Detalle_Post.as_view(), name='detalle-post')
    
]