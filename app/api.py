from .models import Aula, Materia, Profesor
from rest_framework import viewsets, permissions
from .serializers import AulaSerializer, MateriaSerializer, ProfesorSerializer

class ProfesorViewSet(viewsets.ModelViewSet):
    queryset = Profesor.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProfesorSerializer

class MateriaViewSet(viewsets.ModelViewSet):
    queryset = Materia.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MateriaSerializer

class AulaViewSet(viewsets.ModelViewSet):
    queryset = Aula.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AulaSerializer