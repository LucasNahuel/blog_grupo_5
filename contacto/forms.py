from django import forms
from .models import MensajeContacto

class ContactoForm(forms.ModelForm):
    class Meta:
        model=MensajeContacto
        fields=['nombre', 'mensaje', 'correo']
        widgets={
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'mensaje': forms.Textarea(attrs={'class':'form-control'}),
            'correo': forms.TextInput(attrs={'class':'form-control'})
        }