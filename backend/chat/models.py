from django.conf import settings
from django.db import models


class Canal(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.CharField(max_length=200, blank=True)
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='canales')
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['nombre']
        verbose_name_plural = 'canales'

    def __str__(self):
        return f'#{self.nombre}'


class Mensaje(models.Model):
    canal = models.ForeignKey(Canal, on_delete=models.CASCADE, related_name='mensajes')
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='mensajes')
    texto = models.TextField()
    creado = models.DateTimeField(auto_now_add=True)
    # Vacío mientras el mensaje no se haya editado.
    editado = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-creado']

    def __str__(self):
        return f'{self.autor}: {self.texto[:40]}'
