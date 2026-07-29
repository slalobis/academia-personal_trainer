from modelos.treino import Treino
from interfaces.monitoramento import Monitoramento


class TreinoForca(Treino, Monitoramento):

    def __init__(self, duracao, peso_levantado, series):
        Treino.__init__(self, duracao)
        Monitoramento.__init__(self)

        self.peso_levantado = peso_levantado
        self.series = series

    @property
    def peso_levantado(self):
        return self.__peso_levantado

    @peso_levantado.setter
    def peso_levantado(self, valor):
        if valor <= 0:
            raise ValueError("O peso deve ser maior que zero.")
        self.__peso_levantado = valor

    @property
    def series(self):
        return self.__series

    @series.setter
    def series(self, valor):
        if valor <= 0:
            raise ValueError("O número de séries deve ser maior que zero.")
        self.__series = valor

    def calcular_calorias(self):
        return self.peso_levantado * self.series * 0.15

    def nivel_dificuldade(self):

        if self.peso_levantado < 30:
            return "Iniciante"

        elif self.peso_levantado < 70:
            return "Intermediário"

        return "Avançado"