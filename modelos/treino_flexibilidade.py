from modelos.treino import Treino


class TreinoFlexibilidade(Treino):
    """
    Classe que representa um treino de flexibilidade.
    """

    def __init__(self, duracao, nivel_alongamento):
        super().__init__(duracao)

        self.nivel_alongamento = nivel_alongamento

    # -------------------------
    # Encapsulamento
    # -------------------------

    @property
    def nivel_alongamento(self):
        return self.__nivel_alongamento

    @nivel_alongamento.setter
    def nivel_alongamento(self, valor):
        if valor < 1 or valor > 10:
            raise ValueError(
                "O nível de alongamento deve estar entre 1 e 10."
            )
        self.__nivel_alongamento = valor

    # -------------------------
    # Polimorfismo
    # -------------------------

    def calcular_calorias(self):
        """
        Calcula o gasto calórico do treino.
        """
        return self.duracao * 2

    def nivel_dificuldade(self):
        """
        Define o nível de dificuldade do treino.
        """
        if self.nivel_alongamento <= 3:
            return "Iniciante"

        elif self.nivel_alongamento <= 7:
            return "Intermediário"

        return "Avançado"

    # -------------------------
    # Método exclusivo
    # -------------------------

    def ganho_mobilidade(self):
        """
        Calcula o ganho de mobilidade.
        """
        return self.duracao * self.nivel_alongamento * 0.5

    # -------------------------
    # Método auxiliar
    # -------------------------

    def exibir_dados(self):
        print("=== Treino de Flexibilidade ===")
        print(f"Duração: {self.duracao} minutos")
        print(f"Nível de alongamento: {self.nivel_alongamento}")
        print(f"Dificuldade: {self.nivel_dificuldade()}")
        print(f"Calorias: {self.calcular_calorias():.2f} kcal")
        print(f"Ganho de mobilidade: {self.ganho_mobilidade():.1f}")
