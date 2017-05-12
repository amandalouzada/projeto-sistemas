from django.db import models



class Classe(models.Model):
    nome = models.CharField(max_length = 20)
    desconto = models.DecimalField(max_digits=5, decimal_places=2)
    descricao = models.CharField(max_length = 200)


    def __str__(self):
        return '{0} - {1}'.format(self.nome, self.desconto)
