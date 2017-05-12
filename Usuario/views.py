from Usuario.models import Usuario
from Usuario.serializers import *
from rest_framework import generics
from django.contrib.auth.models import User, Group
from rest_framework import  viewsets


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class UsuarioList(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class UsuarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
