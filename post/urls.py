from .views import Lista_post, Crear_post, Editar_post, Eliminar_post, Detalle_Post,BorrarComentarioView,EditarComentarioView, Buscar_post
from django.urls import path


urlpatterns = [
    path('', Lista_post.as_view(), name='posts'),
    path('crear/', Crear_post.as_view(), name="crear_post"),
    path('editar/<int:pk>', Editar_post.as_view(), name="editar_post"),
    path('eliminar/<int:pk>', Eliminar_post.as_view(), name="eliminar_post"),
    path('detalle/<int:pk>', Detalle_Post.as_view(), name='detalle_post'),
    path('borrar_comentario/<int:pk>', BorrarComentarioView.as_view(), name="borrar_comentario"),
    path('editar_comentario/<int:pk>', EditarComentarioView.as_view(), name="editar_comentario"),
    path('buscar/', Buscar_post, name="buscar_post")
]