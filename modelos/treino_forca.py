from treino import Treino

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

        return self.peso * self.series * 0.15

    def descricao(self):

        return (
            f"Tipo: Força\n"
            f"Exercício: {self.exercicio}\n"
            f"Nível: {self.nivel}\n"
            f"Séries: {self.series}\n"
            f"Repetições: {self.repeticoes}\n"
            f"Peso: {self.peso} kg\n"
            f"Calorias queimadas: "
            f"{self.calcular_calorias():.2f} kcal"
        )
