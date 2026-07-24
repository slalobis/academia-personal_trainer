from abc import ABC, abstractmethod

# ==========================
# Classe Abstrata Treino
# ==========================

class Treino(ABC):

    NIVEIS = ("iniciante", "intermediario", "avancado")

    def __init__(self, nivel):
        nivel = nivel.lower()

        if nivel not in self.NIVEIS:
            raise ValueError(
                "Nível inválido. Use: iniciante, intermediario ou avancado."
            )

        self.nivel = nivel

    @abstractmethod
    def calcular_calorias(self):
        pass


# ==========================
# Tipos de Treino
# ==========================

class TreinoForca(Treino):

    def __init__(self, peso_levantado, series, nivel):
        super().__init__(nivel)

        self.peso_levantado = peso_levantado
        self.series = series

    def calcular_calorias(self):
        return self.peso_levantado * self.series * 0.15


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


# ==========================
# Classe Aluno
# ==========================

class Aluno:

    def __init__(self, nome, meses_matriculado):
        self.nome = nome
        self.meses_matriculado = meses_matriculado
        self.plano = PlanoSemanal()

    def adicionar_treino(self, treino):

        # Menos de 1 mês:
        # apenas treinos iniciantes
        if self.meses_matriculado < 1:

            if treino.nivel != "iniciante":
                print(
                    f"{self.nome} não pode realizar treinos "
                    "intermediários ou avançados."
                )
                return

        # Entre 1 e 3 meses:
        # iniciante e intermediário
        elif self.meses_matriculado < 3:

            if treino.nivel == "avancado":
                print(
                    f"{self.nome} ainda não pode realizar "
                    "treinos avançados."
                )
                return

        # Adiciona ao plano semanal
        if self.plano.adicionar_treino(treino):

            print(
                f"Treino {treino.nivel} adicionado "
                f"para {self.nome}."
            )

        else:

            print(
                f"{self.nome} atingiu o limite de "
                f"{PlanoSemanal.LIMITE_TREINOS} treinos na semana."
            )

    def mostrar_plano(self):

        print("\n==============================")
        print(f"Plano semanal de {self.nome}")
        print("==============================")

        if not self.plano.treinos:
            print("Nenhum treino cadastrado.")
            return

        for indice, treino in enumerate(self.plano.treinos, 1):

            print(f"\nTreino {indice}: {treino.__class__.__name__}")
            print(f"Nível: {treino.nivel}")
            print(f"Calorias: {treino.calcular_calorias():.2f}")

            if isinstance(treino, TreinoFlexibilidade):
                print(
                    f"Ganho de mobilidade: "
                    f"{treino.calcular_mobilidade():.2f}"
                )

        print("\n------------------------------")
        print(
            f"Total semanal de calorias: "
            f"{self.plano.calcular_calorias_semana():.2f}"
        )
        print("------------------------------")


# ==========================
# TESTE DO SISTEMA
# ==========================

carlos = Aluno("Carlos", 0)
ana = Aluno("Ana", 3)

# Treinos

forca_iniciante = TreinoForca(50, 3, "iniciante")
cardio_iniciante = TreinoCardio(30, 5, "iniciante")
flexibilidade_iniciante = TreinoFlexibilidade(40, "iniciante")

forca_intermediario = TreinoForca(80, 5, "intermediario")
cardio_intermediario = TreinoCardio(45, 7, "intermediario")
flexibilidade_intermediario = TreinoFlexibilidade(60, "intermediario")

forca_avancado = TreinoForca(100, 8, "avancado")
cardio_avancado = TreinoCardio(60, 10, "avancado")
flexibilidade_avancado = TreinoFlexibilidade(90, "avancado")

# ==========================
# Carlos
# ==========================

carlos.adicionar_treino(forca_iniciante)
carlos.adicionar_treino(cardio_iniciante)
carlos.adicionar_treino(forca_intermediario)      # Bloqueado
carlos.adicionar_treino(cardio_avancado)          # Bloqueado
carlos.adicionar_treino(flexibilidade_iniciante)
carlos.adicionar_treino(flexibilidade_avancado)   # Bloqueado

carlos.mostrar_plano()

# ==========================
# Ana
# ==========================

ana.adicionar_treino(forca_intermediario)
ana.adicionar_treino(forca_avancado)
ana.adicionar_treino(cardio_intermediario)
ana.adicionar_treino(cardio_avancado)
ana.adicionar_treino(flexibilidade_intermediario)

# Excede o limite semanal (6º treino)
ana.adicionar_treino(flexibilidade_avancado)

ana.mostrar_plano()
