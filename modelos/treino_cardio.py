from modelos.treino import Treino
from interfaces.monitoramento import Monitoramento


class TreinoCardio(Treino, Monitoramento):
    """
    Classe que representa um treino cardiovascular.
    Herda da classe Treino e da classe Monitoramento.
    """

    def __init__(self, duracao, intensidade):
        Treino.__init__(self, duracao)
        Monitoramento.__init__(self)

        self.intensidade = intensidade

    # -------------------------
    # Encapsulamento
    # -------------------------

    @property
    def intensidade(self):
        return self.__intensidade

    @intensidade.setter
    def intensidade(self, valor):
        if valor < 1 or valor > 10:
            raise ValueError("A intensidade deve estar entre 1 e 10.")
        self.__intensidade = valor

    # -------------------------
    # Polimorfismo
    # -------------------------

    def calcular_calorias(self):
        """
        Calcula o gasto calórico do treino cardio.
        """
        return self.duracao * self.intensidade * 8

    def nivel_dificuldade(self):
        """
        Define a dificuldade considerando a intensidade.
        """
        if self.intensidade <= 3:
            return "Iniciante"

        elif self.intensidade <= 7:
            return "Intermediário"

        return "Avançado"

    # -------------------------
    # Método auxiliar
    # -------------------------

    def exibir_dados(self):
        print("=== Treino Cardio ===")
        print(f"Duração: {self.duracao} minutos")
        print(f"Intensidade: {self.intensidade}")
        print(f"Dificuldade: {self.nivel_dificuldade()}")
        print(f"Calorias: {self.calcular_calorias():.2f} kcal")
