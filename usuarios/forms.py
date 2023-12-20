from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import Usuario

class RegistrarseForm(UserCreationForm):

    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'align':'center', 'placeholder':'contraseña'}),
    )
    password2 = forms.CharField(
        label="Confirmar contraseña",
        widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'align':'center', 'placeholder':'contraseña'}),
    )

    class Meta:
        model=Usuario
        fields=['first_name', 'last_name', 'username', 'password1', 'password2', 'email','telefono', 'domicilio','imagen_perfil']
        widgets={
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'telefono': forms.TextInput(attrs={'class':'form-control'}),
            'domicilio': forms.TextInput(attrs={'class':'form-control'}),
            'imagen_perfil': forms.ClearableFileInput(attrs={'class': 'form-control'})
        }

class UserLoginForm(AuthenticationForm):

    username = forms.CharField(
        label="Usuario",
        widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'text', 'align':'center', 'placeholder':'usuario'}),
    )

    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'align':'center', 'placeholder':'contraseña'}),
    )

    class Meta:
        model=Usuario
        fields=['username', 'password']
       
class EditarPerfilForm(forms.ModelForm):
    class Meta:
        model=Usuario
        fields=['first_name', 'last_name', 'email', 'domicilio','telefono','imagen_perfil']
        widgets={
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'telefono': forms.TextInput(attrs={'class':'form-control'}),
            'domicilio': forms.TextInput(attrs={'class':'form-control'}),
            'imagen_perfil': forms.ClearableFileInput(attrs={'class':'form-control'})
        }