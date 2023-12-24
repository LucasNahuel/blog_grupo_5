from django.urls import path
from .views import form_contacto, Listar_contactos, Eliminar_mensaje_contacto

urlpatterns = [
    path('', form_contacto, name='form_contacto'),
    path('mensajes/', Listar_contactos.as_view(), name='lista_mensajes' ),
    path('mensajes/eliminar/<int:pk>', Eliminar_mensaje_contacto.as_view(), name='eliminar_mensaje')
]
