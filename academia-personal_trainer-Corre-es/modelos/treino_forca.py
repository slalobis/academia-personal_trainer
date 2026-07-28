from modelos.treino import Treino
from modelos.dificuldade import Dificuldade

class TreinoForca(Treino, Dificuldade):

    def __init__(self, peso_levantado, series, vezes_levantado, nivel):
        super().__init__(nivel)

        self.__peso_levantado = peso_levantado
        self.__series = series
        self.__vezes_levantado = vezes_levantado

    @property
    def peso_levantado(self):
        return self.__peso_levantado
    
    @property
    def vezes_levantado(self):
        return self.__vezes_levantado

    @property
    def series(self):
        return self.__series

    def calcular_calorias(self):
        return self.__peso_levantado * self.__series * 0.15

    def descricao(self):
        return (f"Treino de Força\n"
            f"Séries: {self.series} x {self.vezes_levantado}\n"
            f"Peso: {self.peso_levantado} kg")
