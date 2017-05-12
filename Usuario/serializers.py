from rest_framework import serializers
from Classe.models import *
from Usuario.models import *
from django.contrib.auth.models import User, Group

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')



class UsuarioSerializerD(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id')


class UsuarioSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializerD(read_only=True)

    class Meta:
        model = Usuario
        fields = ('usuario','matricula', 'cpf')
