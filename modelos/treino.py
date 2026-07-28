from abc import ABC, abstractmethod

# ==========================
# Classe Abstrata Treino
# ==========================

class Treino(ABC):

    NIVEIS = ("iniciante", "intermediario", "avancado")

    def __init__(self, nivel):

        nivel = nivel.lower()

        if nivel not in self.NIVEIS:
            raise ValueError("Nível inválido.")

        self.__nivel = nivel   # atributo privado

    @property
    def nivel(self):
        return self.__nivel

    @abstractmethod
    def calcular_calorias(self):
        pass
