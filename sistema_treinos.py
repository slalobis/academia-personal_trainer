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
        # cálculo baseado no peso levantado e séries
        return self.peso_levantado * self.series * 0.15


class TreinoCardio(Treino):

    def __init__(self, tempo, intensidade, nivel):
        super().__init__(nivel)

        self.tempo = tempo
        self.intensidade = intensidade

    def calcular_calorias(self):
        # cálculo baseado no tempo e intensidade
        return self.tempo * self.intensidade * 8


class TreinoFlexibilidade(Treino):

    def __init__(self, tempo, nivel):
        super().__init__(nivel)

        self.tempo = tempo

    def calcular_calorias(self):
        # Flexibilidade gasta menos calorias
        return self.tempo * 2

    def calcular_mobilidade(self):
        # Apenas flexibilidade possui ganho de mobilidade
        return self.tempo * 1.5


# ==========================
# Plano Semanal
# ==========================

class PlanoSemanal:

    def __init__(self):
        self.treinos = []

    def adicionar_treino(self, treino):
        self.treinos.append(treino)

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
        # só pode fazer treinos iniciantes
        if self.meses_matriculado < 1:

            if treino.nivel != "iniciante":
                print(
                    f"{self.nome} não pode realizar treinos "
                    "intermediários ou avançados."
                )
                return


        # Entre 1 e 3 meses:
        # pode fazer iniciante e intermediário
        elif self.meses_matriculado < 3:

            if treino.nivel == "avancado":
                print(
                    f"{self.nome} ainda não pode realizar "
                    "treinos avançados."
                )
                return


        self.plano.adicionar_treino(treino)

        print(
            f"Treino {treino.nivel} adicionado "
            f"para {self.nome}."
        )


    def mostrar_plano(self):

        print("\n==============================")
        print(f"Plano semanal de {self.nome}")
        print("==============================")

        for indice, treino in enumerate(self.plano.treinos, 1):

            print(
                f"\nTreino {indice}: "
                f"{treino.__class__.__name__}"
            )

            print(
                f"Nível: {treino.nivel}"
            )

            print(
                f"Calorias: "
                f"{treino.calcular_calorias():.2f}"
            )


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


# Carlos possui 0 meses de matrícula
carlos = Aluno("Carlos", 0)


# Criando treinos

forca_iniciante = TreinoForca(
    peso_levantado=50,
    series=3,
    nivel="iniciante"
)


cardio_iniciante = TreinoCardio(
    tempo=30,
    intensidade=5,
    nivel="iniciante"
)

flexibilidade_iniciante = TreinoFlexibilidade(
    tempo=40,
    nivel="iniciante"
)

forca_intermediario = TreinoForca(
    peso_levantado=80,
    series=5,
    nivel="intermediario"
)

cardio_intermediario = TreinoCardio(
    tempo=45,
    intensidade =7,
    nivel="intermediario"
)

flexibilidade_intermediario = TreinoFlexibilidade(
    tempo=60,
    nivel="intermediario"
)

forca_avancado = TreinoForca(
    peso_levantado=100,
    series=8,
    nivel="avancado"
)

cardio_avancado = TreinoCardio(
    tempo=60,
    intensidade=10,
    nivel="avancado"
)

flexibilidade_avancado = TreinoFlexibilidade(
    tempo=90,
    nivel="avancado"
)

# Adicionando treinos ao plano semanal

print("")

carlos.adicionar_treino(forca_iniciante)
carlos.adicionar_treino(cardio_iniciante)

# Será bloqueado (Carlos tem menos de 1 mês)
carlos.adicionar_treino(forca_intermediario)

# Será bloqueado (Carlos tem menos de 1 mês)
carlos.adicionar_treino(cardio_avancado)

carlos.adicionar_treino(flexibilidade_iniciante)
#Será bloqueado (Carlos tem menos de 1 mês)
carlos.adicionar_treino(flexibilidade_avancado)


# Mostra o plano final
carlos.mostrar_plano()
