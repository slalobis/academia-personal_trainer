from treino import Treino
from dificuldade import Dificuldade


class TreinoForca(Treino):

    def __init__(self,
                 exercicio,
                 peso,
                 series,
                 repeticoes,
                 nivel,
                 dificuldade):

        super().__init__(nivel)

        self.__exercicio = exercicio
        self.__peso = peso
        self.__series = series
        self.__repeticoes = repeticoes
        self.__dificuldade = dificuldade

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

    @property
    def dificuldade(self):
        return self.__dificuldade

    def descricao(self):

        return (
            f"{self.exercicio}\n"
            f"Nível: {self.nivel}\n"
            f"Dificuldade: {self.dificuldade.value}"
        )
