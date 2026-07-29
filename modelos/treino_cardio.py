from modelos.treino import Treino
from modelos.avaliavel import Avaliavel

class TreinoCardio(Treino, Avaliavel):

    def __init__(self, atividade, tempo, intensidade, nivel):

        super().__init__(nivel)

        self.__atividade = atividade
        self.__tempo = tempo
        self.__intensidade = intensidade

    @property
    def atividade(self):
        return self.__atividade

    @property
    def tempo(self):
        return self.__tempo

    @property
    def intensidade(self):
        return self.__intensidade

    def calcular_calorias(self):

        fatores = {
            "leve": 1,
            "moderada": 2,
            "intensa": 3
        }

        fator = fatores.get(self.intensidade.lower(), 1)

        return self.tempo * fator * 8

    def descricao(self):

        return (
            f"Tipo: Cardio\n"
            f"Atividade: {self.atividade}\n"
            f"Nível: {self.nivel}\n"
            f"Tempo: {self.tempo} minutos\n"
            f"Intensidade: {self.intensidade}\n"
            f"Calorias queimadas: "
            f"{self.calcular_calorias():.2f} kcal"
        )

    def recomendacao(self):
        return "Mantenha-se hidratado durante o treino."
