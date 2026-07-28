from modelos.treino import Treino
from modelos.avaliavel import Avaliavel

class TreinoFlexibilidade(Treino, Avaliavel):

    def __init__(self,
                 alongamento,
                 tempo,
                 nivel):

        super().__init__(nivel)

        self.__alongamento = alongamento
        self.__tempo = tempo

    @property
    def alongamento(self):
        return self.__alongamento

    @property
    def tempo(self):
        return self.__tempo

    def calcular_calorias(self):

        return self.tempo * 2

    def calcular_mobilidade(self):

        return self.tempo * 1.5

    def descricao(self):
        return (
            f"Treino de Flexibilidade: {self.nome} | "
            f"{self.tempo} minutos de alongamento.\n"
            f"Nível: {self.nivel_dificuldade()}\n"
            f"{self.recomendacao()}"
        )
        
    def nivel_dificuldade(self):
        return "Leve"

    def recomendacao(self):
        return "Realize os alongamentos lentamente e sem ultrapassar seus limites."
