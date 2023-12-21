from django.contrib.auth.mixins import UserPassesTestMixin

class Superuser_mixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser
    
