from django.shortcuts import render, redirect
from .forms import ContactoForm
from django.contrib import messages
from .models import MensajeContacto


# Create your views here.
        

def form_contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mensaje enviado correctamente.')
            return redirect('form_contacto')
    else:
        form = ContactoForm()

    # Obtener todos los mensajes para mostrarlos al administrador
    
    mensajes = MensajeContacto.objects.all()

    return render(request, 'contacto/form_contacto.html', {'form': form, 'mensajes': mensajes})
