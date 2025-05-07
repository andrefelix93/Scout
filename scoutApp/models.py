from django.db import models

# Create your models here.
from django.db import models

class Partida(models.Model):
    time_casa = models.CharField(max_length=100)
    time_fora = models.CharField(max_length=100)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.time_casa} x {self.time_fora} ({self.data.strftime('%d/%m/%Y')})"


class Acao(models.Model):
    jogador = models.CharField(max_length=100)
    tipo_acao = models.CharField(max_length=100)
    pos_x = models.FloatField()
    pos_y = models.FloatField()
    tempo = models.IntegerField(choices=[(1, "1º Tempo"), (2, "2º Tempo")])  # <- NOVO
    partida = models.ForeignKey(Partida, on_delete=models.CASCADE)  # <- NOVO

    def __str__(self):
        return f"{self.jogador} - {self.tipo_acao} em ({self.pos_x}, {self.pos_y}) no {self.tempo}, jogo: {self.partida}"
