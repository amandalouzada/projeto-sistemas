from django.db import models
from django.contrib.auth.models import User
from Classe.models import *
from datetime import datetime
from Financeiro.models import *

STATUS = (
    (1,"ATIVO"),
    (0,"BLOQUEADO")
)

class Cartao(models.Model):
    rfid = models.CharField(max_length = 11)
    status = models.IntegerField(choices=STATUS, default=0)


class Conta(models.Model):
    saldo = models.DecimalField(max_digits=5, decimal_places=2)

class Usuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    matricula = models.CharField(max_length = 11)
    cpf = models.CharField(max_length = 11)
    conta = models.ForeignKey(Conta, null=False)

    def __str__(self):
        return '{0} - {1}'.format(self.matricula, self.cpf)



class ClasseUsuario(models.Model):
     usuario = models.ForeignKey(Usuario, null=False)
     classe  = models.ForeignKey(Classe, null=False)
     data_inicio = models.DateField(default=datetime.now)
     data_fim = models.DateField(null=True, blank=True)


class CartaoUsuario(models.Model):
     usuario = models.ForeignKey(Usuario, null=False)
     cartao  = models.ForeignKey(Cartao, null=False)
     data_inicio = models.DateField(default=datetime.now)
     data_fim = models.DateField(null=True, blank=True)
