from django.db import models
TIPO_PERIODO = (
    (1,"MANHÃ"),
    (2,"TARDE"),
    (3,"NOITE")
)

# Create your models here.
class Refeicao(models.Model):
    nome = models.CharField(max_length = 20)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    periodo = models.IntegerField(choices=TIPO_PERIODO, default=2)


    def __str__(self):
        return '{0} - {1}'.format(self.nome, self.preco)
