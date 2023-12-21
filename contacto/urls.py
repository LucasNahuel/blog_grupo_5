from django.urls import path
from .views import form_contacto, Listar_contactos

urlpatterns = [
    path('', form_contacto, name='form_contacto'),
    path('mensajes/', Listar_contactos.as_view(), name='lista_mensajes' )
]
