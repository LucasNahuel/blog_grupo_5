from django import forms
from .models import post

class Crear_post(forms.ModelForm):
    class Meta:
        model = post
        fields = ['titulo', 'cuerpo', 'categoria', 'creador']
        widgets = {
            'titulo': forms.TextInput(attrs={'class':'form-control'}),
            'cuerpo': forms.Textarea(attrs={'class':'form-control'}),
            'categoria': forms.TextInput(attrs={'class':'form-control'}),
            'creador': forms.TextInput(attrs={'class':'form-control'}),
        }