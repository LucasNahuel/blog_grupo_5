from django.urls import path
from .views import form_contacto

urlpatterns = [
    path('', form_contacto, name='form_contacto'),
  
]
