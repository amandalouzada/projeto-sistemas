from Classe.models import Classe
from Classe.serializers import ClasseSerializer
from rest_framework import generics


class ClasseList(generics.ListCreateAPIView):
    queryset = Classe.objects.all()
    serializer_class = ClasseSerializer


class ClasseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Classe.objects.all()
    serializer_class = ClasseSerializer
