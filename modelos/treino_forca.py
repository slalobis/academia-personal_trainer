from modelos.treino import Treino

class TreinoForca(Treino):

    def __init__(self,
                 exercicio,
                 peso,
                 series,
                 repeticoes,
                 nivel):

        super().__init__(nivel)

        self.__exercicio = exercicio
        self.__peso = peso
        self.__series = series
        self.__repeticoes = repeticoes

    @property
    def exercicio(self):
        return self.__exercicio

    @property
    def peso(self):
        return self.__peso

    @property
    def series(self):
        return self.__series

    @property
    def repeticoes(self):
        return self.__repeticoes

    def calcular_calorias(self):

        return self.peso * self.series * self.repeticoes * 0.15

    def descricao(self):
        return (
            f"Treino de Força: {self.nome} | "
            f"{self.series} séries x {self.repeticoes} repetições "
            f"com {self.peso} kg.\n"
            f"Nível: {self.nivel_dificuldade()}\n"
            f"{self.recomendacao()}"
        )
