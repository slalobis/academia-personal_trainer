from .treino import Treino
from interfaces.monitoramento import Monitoramento


class TreinoCardio(Treino, Monitoramento):

    def __init__(self, duracao, intensidade):
        Treino.__init__(self, duracao)
        Monitoramento.__init__(self)

        self.intensidade = intensidade

    @property
    def intensidade(self):
        return self.__intensidade

    @intensidade.setter
    def intensidade(self, valor):
        if not 1 <= valor <= 10:
            raise ValueError("A intensidade deve estar entre 1 e 10.")
        self.__intensidade = valor

    def calcular_calorias(self):
        return self.duracao * self.intensidade * 8

    def nivel_dificuldade(self):

        if self.intensidade <= 3:
            return "Iniciante"

        elif self.intensidade <= 7:
            return "Intermediário"

        return "Avançado"
