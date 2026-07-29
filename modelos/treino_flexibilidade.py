from modelos.treino import Treino
from modelos.avaliavel import Avaliavel

class TreinoFlexibilidade(Treino, Avaliavel):

    def __init__(self, alongamento, tempo, nivel):

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
            f"Tipo: Flexibilidade\n"
            f"Alongamento: {self.alongamento}\n"
            f"Nível: {self.nivel}\n"
            f"Tempo: {self.tempo} segundos\n"
            f"Mobilidade adquirida: "
            f"{self.calcular_mobilidade():.2f}\n"
            f"Calorias queimadas: "
            f"{self.calcular_calorias():.2f} kcal"
        )

    def recomendacao(self):
        return "Realize os alongamentos lentamente."
