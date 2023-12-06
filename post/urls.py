from .views import Lista_post, Crear_post
from django.urls import path


urlpatterns = [
    path('', Lista_post.as_view(), name='posts'),
    path('crear/', Crear_post.as_view(), name="crear_post")
]