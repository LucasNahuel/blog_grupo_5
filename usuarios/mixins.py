from django.contrib.auth.mixins import UserPassesTestMixin

class Propietario_perfil(UserPassesTestMixin):
    def test_func(self):
        return self.get_object() == self.request.user or self.request.user.is_superuser
    
