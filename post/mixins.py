from django.contrib.auth.mixins import UserPassesTestMixin
from .models import post, Comentario

class Colaborador_mixin(UserPassesTestMixin):
    def test_func(self):
        usuario = self.request.user
        return usuario.es_colaborador or usuario.is_superuser
    
class Creador_mixin(UserPassesTestMixin):
    def test_func(self):
        usuario = self.request.user
        objeto = self.get_object()

        if isinstance(object, post):
            return usuario == objeto.creador or usuario.is_superuser
        elif isinstance(objeto, Comentario):
            return usuario == objeto.creador or usuario.is_superuser or usuario == objeto.publicacion.creador