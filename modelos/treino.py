from abc import ABC, abstractmethod

class Treino(ABC):

    def __init__(self, nivel):

        self.__nivel = nivel

    @property
    def nivel(self):
        return self.__nivel

    @abstractmethod
    def descricao(self):
        pass

    @abstractmethod
    def calcular_calorias(self):
        pass

    def __str__(self):

        return self.descricao()
