from django import forms
from .models import post, Comentario

class Crear_post(forms.ModelForm):
    class Meta:
        model = post
        fields = ['titulo', 'cuerpo', 'categoria', 'imagen']
        widgets = {
            'titulo': forms.TextInput(attrs={'class':'form-control'}),
            'cuerpo': forms.Textarea(attrs={'class':'form-control'}),
            'categoria': forms.Select(attrs={'class':'form-select'}),
        }

class ComentarioForm(forms.ModelForm):
    class Meta:
        model=Comentario
        fields=['texto']
        widgets = {
            'texto': forms.Textarea(attrs={'class':'form-control'})
        }
        labels ={
            'texto':''
        }