from django.db import models

# Create your models here.


class MensajeContacto(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    mensaje = models.TextField()
    
    def __str__(self):
        return f'{self.nombre} - {self.correo}'