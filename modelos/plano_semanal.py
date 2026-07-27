class PlanoSemanal:

    LIMITE_TREINOS = 5

    def __init__(self):
        self.treinos = []

    def adicionar_treino(self, treino):

        if len(self.treinos) >= self.LIMITE_TREINOS:
            return False

        self.treinos.append(treino)
        return True

    def calcular_calorias_semana(self):

        total = 0

        for treino in self.treinos:
            total += treino.calcular_calorias()

        return total
