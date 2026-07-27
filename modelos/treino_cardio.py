from modelos.treino import Treino

class TreinoCardio(Treino):

    def __init__(self, tempo, intensidade, nivel):
        super().__init__(nivel)

        self.tempo = tempo
        self.intensidade = intensidade

    def calcular_calorias(self):
        return self.tempo * self.intensidade * 8
