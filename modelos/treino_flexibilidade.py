from modelos.treino import Treino

class TreinoFlexibilidade(Treino):

    def __init__(self, tempo, nivel):
        super().__init__(nivel)

        self.__tempo = tempo

    @property
    def tempo(self):
        return self.__tempo

    def calcular_calorias(self):
        return self.tempo * 2

    def calcular_mobilidade(self):
        return self.tempo * 1.5
