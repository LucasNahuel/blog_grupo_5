from django.shortcuts import render, redirect
from .forms import ContactoForm
from django.contrib import messages
from .models import MensajeContacto
from django.views.generic import ListView
from .mixins import Superuser_mixin
from django.urls import reverse
# Create your views here.
        

def form_contacto(request):

    if request.user.is_superuser:
        return redirect('lista_mensajes')

    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Mensaje enviado correctamente.", "alert alert-success alert-dismissible fade show")

            return redirect('form_contacto')
    else:
        form = ContactoForm()

    # Obtener todos los mensajes para mostrarlos al administrador
    
    mensajes = MensajeContacto.objects.all()

    return render(request, 'contacto/form_contacto.html', {'form': form, 'mensajes': mensajes})


class Listar_contactos(Superuser_mixin, ListView):
    template_name = 'contacto/lista_mensajes.html'
    model = MensajeContacto
    context_object_name = 'mensajes'
