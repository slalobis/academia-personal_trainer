from abc import ABC, abstractmethod
from datetime import date

# ==========================
# Classe Abstrata
# ==========================

class Treino(ABC):

    NIVEIS = ("iniciante", "intermediario", "avancado")

    def __init__(self, nivel):
        nivel = nivel.lower()

        if nivel not in self.NIVEIS:
            raise ValueError("Nível inválido! Use: iniciante, intermediario ou avancado.")

        self.nivel = nivel

    @abstractmethod
    def calcular_calorias(self):
        pass


# ==========================
# Classes Filhas
# ==========================

class TreinoForca(Treino):

    def __init__(self, peso, series, nivel):
        super().__init__(nivel)
        self.peso = peso
        self.series = series

    def calcular_calorias(self):
        return self.peso * self.series * 0.15


class TreinoCardio(Treino):

    def __init__(self, tempo, intensidade, nivel):
        super().__init__(nivel)
        self.tempo = tempo
        self.intensidade = intensidade

    def calcular_calorias(self):
        return self.tempo * self.intensidade * 8


class TreinoFlexibilidade(Treino):

    def __init__(self, tempo, nivel):
        super().__init__(nivel)
        self.tempo = tempo

    def calcular_calorias(self):
        return self.tempo * 2

    def calcular_mobilidade(self):
        return self.tempo * 1.5


# ==========================
# Plano Semanal
# ==========================

class PlanoSemanal:

    def __init__(self):
        self.treinos = []

    def adicionar_treino(self, treino):
        self.treinos.append(treino)

    def calorias_totais(self):
        total = 0

        for treino in self.treinos:
            total += treino.calcular_calorias()

        return total


# ==========================
# Classe Aluno
# ==========================

class Aluno:

    def __init__(self, nome, data_matricula):
        self.nome = nome
        self.data_matricula = data_matricula
        self.plano = PlanoSemanal()

    def meses_matriculado(self):
        dias = (date.today() - self.data_matricula).days
        return dias / 30

    def adicionar_treino(self, treino):

        meses = self.meses_matriculado()

        # Menos de 1 mês → somente iniciante
        if meses < 1 and treino.nivel != "iniciante":
            print(f"{self.nome}: apenas treinos INICIANTES são permitidos.")
            return

        # Entre 1 e 3 meses → iniciante e intermediário
        if 1 <= meses < 3 and treino.nivel == "avancado":
            print(f"{self.nome}: treinos AVANÇADOS só são permitidos após 3 meses.")
            return

        self.plano.adicionar_treino(treino)
        print("Treino adicionado com sucesso!")

    def mostrar_plano(self):

        print(f"\n===== Plano semanal de {self.nome} =====")

        for i, treino in enumerate(self.plano.treinos, start=1):

            if isinstance(treino, TreinoForca):
                print(f"{i}. Força ({treino.nivel})")
                print(f"   Calorias: {treino.calcular_calorias():.2f}")

            elif isinstance(treino, TreinoCardio):
                print(f"{i}. Cardio ({treino.nivel})")
                print(f"   Calorias: {treino.calcular_calorias():.2f}")

            elif isinstance(treino, TreinoFlexibilidade):
                print(f"{i}. Flexibilidade ({treino.nivel})")
                print(f"   Calorias: {treino.calcular_calorias():.2f}")
                print(f"   Ganho de mobilidade: {treino.calcular_mobilidade():.2f}")

        print("-----------------------------------")
        print(f"Total de calorias da semana: {self.plano.calorias_totais():.2f}")
        print("-----------------------------------")


# ==========================
# Exemplo de Uso
# ==========================

# Aluno matriculado recentemente
aluno = Aluno("Carlos", date(2026, 4, 10))

# Plano semanal

# Segunda
treino1 = TreinoForca(50, 3, "iniciante")

# Terça
treino2 = TreinoCardio(25, 5, "iniciante")

# Quarta
treino3 = TreinoForca(80, 5, "intermediario")

# Quinta
treino4 = TreinoCardio(40, 8, "intermediario")

# Sexta
treino5 = TreinoFlexibilidade(30, "iniciante")

# Sábado
treino6 = TreinoForca(120, 6, "avancado")# Será bloqueado(menor que 3 meses)

print("")
# Cadastro dos treinos
aluno.adicionar_treino(treino1)
aluno.adicionar_treino(treino2)
aluno.adicionar_treino(treino3)
aluno.adicionar_treino(treino4)
aluno.adicionar_treino(treino5)
aluno.adicionar_treino(treino6)

# Exibir plano semanal
aluno.mostrar_plano()
