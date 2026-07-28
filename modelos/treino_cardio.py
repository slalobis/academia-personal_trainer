from modelos.treino import Treino
from modelos.avaliavel import Avaliavel

class TreinoCardio(Treino, Avaliavel):

    def __init__(self,
                 atividade,
                 tempo,
                 intensidade,
                 nivel):

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
            f"Treino Cardio: {self.nome} | "
            f"{self.duracao} minutos "
            f"na intensidade {self.intensidade}.\n"
            f"Nível: {self.nivel_dificuldade()}\n"
            f"{self.recomendacao()}"
        )

    def nivel_dificuldade(self):
        return "Moderado"

    def recomendacao(self):
        return "Mantenha-se hidratado durante o treino."
