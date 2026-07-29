from abc import ABC, abstractmethod


class Treino(ABC):
    """
    Classe abstrata que representa um treino genérico.

    Todas as classes de treino devem herdar desta classe e implementar
    os métodos abstratos.
    """

    def __init__(self, duracao):
        self.duracao = duracao  # usa o setter para validar

    # -------------------------
    # Encapsulamento
    # -------------------------

    @property
    def duracao(self):
        return self.__duracao

    @duracao.setter
    def duracao(self, valor):
        if valor <= 0:
            raise ValueError("A duração do treino deve ser maior que zero.")
        self.__duracao = valor

    # -------------------------
    # Métodos Abstratos
    # -------------------------

    @abstractmethod
    def calcular_calorias(self):
        """
        Calcula a quantidade de calorias gastas no treino.
        """
        pass

    @abstractmethod
    def nivel_dificuldade(self):
        """
        Retorna o nível de dificuldade do treino.
        """
        pass

    # -------------------------
    # Método comum
    # -------------------------

    def exibir_informacoes(self):
        print(f"Duração: {self.duracao} minutos")
