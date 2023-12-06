from django import forms
from .models import post

class Crear_post(forms.ModelForm):
    class Meta:
        model = post
        fields = ['titulo', 'cuerpo', 'categoria', 'creador']