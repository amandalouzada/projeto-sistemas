from rest_framework import serializers
from Classe.models import *


class ClasseSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nome = serializers.CharField(max_length = 20)
    desconto = serializers.DecimalField(max_digits=5, decimal_places=2)
    descricao = serializers.CharField(max_length = 200)

    def create(self, validated_data):
        """
        Create and return a new `Classe` instance, given the validated data.
        """
        return Classe.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Classe` instance, given the validated data.
        """
        instance.nome = validated_data.get('nome', instance.nome)
        instance.desconto = validated_data.get('desconto', instance.desconto)
        instance.descricao = validated_data.get('descricao', instance.descricao)
        instance.save()
        return instance
