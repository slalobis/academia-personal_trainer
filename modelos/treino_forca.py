from modelos.treino import Treino

class TreinoForca(Treino):

    def __init__(self, peso_levantado, series, nivel):
        super().__init__(nivel)

        self.peso_levantado = peso_levantado
        self.series = series

    def calcular_calorias(self):
        return self.peso_levantado * self.series * 0.15
