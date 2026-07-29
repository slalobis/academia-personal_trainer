from modelos.treino import Treino


class TreinoForca(Treino):
    """
    Classe que representa um treino de força.
    """

    def __init__(self, duracao, peso_levantado, series):
        super().__init__(duracao)

        self.peso_levantado = peso_levantado
        self.series = series

    # -------------------------
    # Encapsulamento
    # -------------------------

    @property
    def peso_levantado(self):
        return self.__peso_levantado

    @peso_levantado.setter
    def peso_levantado(self, valor):
        if valor <= 0:
            raise ValueError("O peso levantado deve ser maior que zero.")
        self.__peso_levantado = valor

    @property
    def series(self):
        return self.__series

    @series.setter
    def series(self, valor):
        if valor <= 0:
            raise ValueError("O número de séries deve ser maior que zero.")
        self.__series = valor

    # -------------------------
    # Polimorfismo
    # -------------------------

    def calcular_calorias(self):
        """
        Calcula as calorias gastas no treino de força.
        """
        return self.peso_levantado * self.series * 0.15

    def nivel_dificuldade(self):
        """
        Determina o nível de dificuldade do treino.
        """
        if self.peso_levantado < 30:
            return "Iniciante"

        elif self.peso_levantado < 70:
            return "Intermediário"

        return "Avançado"

    # -------------------------
    # Método auxiliar
    # -------------------------

    def exibir_dados(self):
        print("=== Treino de Força ===")
        print(f"Duração: {self.duracao} minutos")
        print(f"Peso levantado: {self.peso_levantado} kg")
        print(f"Séries: {self.series}")
        print(f"Dificuldade: {self.nivel_dificuldade()}")
        print(f"Calorias: {self.calcular_calorias():.2f} kcal")
