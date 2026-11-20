from django.utils import timezone
from rest_framework import viewsets

from .models import Canal, Mensaje
from .serializers import CanalSerializer, MensajeSerializer


class CanalViewSet(viewsets.ModelViewSet):
    queryset = Canal.objects.select_related('creador')
    serializer_class = CanalSerializer

    def perform_create(self, serializer):
        serializer.save(creador=self.request.user)


class MensajeViewSet(viewsets.ModelViewSet):
    queryset = Mensaje.objects.select_related('autor')  # ordenados por -creado (Meta)
    serializer_class = MensajeSerializer
    filterset_fields = ['canal']

    def perform_create(self, serializer):
        serializer.save(autor=self.request.user)

    def perform_update(self, serializer):
        serializer.save(editado=timezone.now())
