from modelos.treino import Treino
from modelos.dificuldade import Dificuldade

class TreinoCardio(Treino, Dificuldade):

    def __init__(self, tempo, intensidade, nivel):
        super().__init__(nivel)

        self.__tempo = tempo
        self.__intensidade = intensidade

    @property
    def tempo(self):
        return self.__tempo

    @property
    def intensidade(self):
        return self.__intensidade

    def calcular_calorias(self):
        return self.tempo * self.intensidade * 8
