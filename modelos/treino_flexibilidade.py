from .treino import Treino
from interfaces.monitoramento import Monitoramento


class TreinoFlexibilidade(Treino, Monitoramento):

    def __init__(self, duracao, nivel_alongamento):
        Treino.__init__(self, duracao)
        Monitoramento.__init__(self)

        self.nivel_alongamento = nivel_alongamento

    @property
    def nivel_alongamento(self):
        return self.__nivel_alongamento

    @nivel_alongamento.setter
    def nivel_alongamento(self, valor):
        if not 1 <= valor <= 10:
            raise ValueError(
                "O nível de alongamento deve estar entre 1 e 10."
            )
        self.__nivel_alongamento = valor

    def calcular_calorias(self):
        return self.duracao * 2

    def nivel_dificuldade(self):

        if self.nivel_alongamento <= 3:
            return "Iniciante"

        elif self.nivel_alongamento <= 7:
            return "Intermediário"

        return "Avançado"
