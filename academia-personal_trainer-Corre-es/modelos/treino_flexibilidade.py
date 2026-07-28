from modelos.treino import Treino
from modelos.dificuldade import Dificuldade

class TreinoFlexibilidade(Treino, Dificuldade):

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
        
    def descricao(self):
        return (f"Treino de Flexibilidade\n"
            f"Tempo: {self.tempo} minutos")
