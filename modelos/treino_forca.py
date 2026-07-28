from modelos.treino import Treino
from modelos.dificuldade import Dificuldade

class TreinoForca(Treino):

    def __init__(self, peso_levantado, series, nivel):
        super().__init__(nivel)

        self.__peso_levantado = peso_levantado
        self.__series = series

    @property
    def peso_levantado(self):
        return self.__peso_levantado

    @property
    def series(self):
        return self.__series

    def calcular_calorias(self):
        return self.__peso_levantado * self.__series * 0.15
