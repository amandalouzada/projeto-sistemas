from django.db import models
from Classe.models import *
from Refeicao.models import *
from Usuario.models import *
from django.contrib.auth.models import User


TIPO_OPERACAO = (
    (1,"DEBITO"),
    (2,"CREDITO")
)



# Create your models here.
class Refeicao(models.Model):
    nome = models.CharField(max_length = 20)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    periodo = models.IntegerField(choices=TIPO_PERIODO, default=2)



# Create your models here.
class Consumo(models.Model):
    cartao = models.ForeignKey(Cartao, null=False)
    usuario = models.ForeignKey(Usuario, null=False)
    classe = models.ForeignKey(Classe, null=False)
    horario = models.DateField(default=datetime.now)
    refeicao = models.ForeignKey(Refeicao, null=False)


class Operacao(models.Model):
    operador = models.ForeignKey(User, null=False)
    conta = models.ForeignKey(Conta, null=False)
    tipo_operacao=models.IntegerField(choices=TIPO_OPERACAO, null=False)
