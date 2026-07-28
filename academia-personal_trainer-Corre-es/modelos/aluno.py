from modelos.plano_semanal import PlanoSemanal
from modelos.treino_flexibilidade import TreinoFlexibilidade

class Aluno:

    def __init__(self, nome, meses_matriculado):
        self.__nome = nome
        self.__meses_matriculado = meses_matriculado
        self.__plano = PlanoSemanal()

    @property
    def nome(self):
        return self.__nome

    @property
    def meses_matriculado(self):
        return self.__meses_matriculado

    @property
    def plano(self):
        return self.__plano
    
    
    def adicionar_treino(self, treino):

        # Menos de 1 mês:
        # apenas treinos iniciantes
        if self.meses_matriculado < 1:

            if treino.nivel != "iniciante":
                print(f"{self.nome} não pode realizar treinos intermediários ou avançados.")
                return

        # Entre 1 e 3 meses:
        # iniciante e intermediário
        elif self.meses_matriculado < 3:

            if treino.nivel == "avancado":
                print(f"{self.nome} ainda não pode realizar treinos avançados.")
                return

        # Adiciona ao plano semanal
        if self.plano.adicionar_treino(treino):

            print(f"Treino {treino.nivel} adicionado para {self.nome}.")

        else:

            print(f"{self.nome} atingiu o limite de {PlanoSemanal.LIMITE_TREINOS} treinos na semana.")

    def mostrar_plano(self):

        print("\n==============================")
        print(f"Plano semanal de {self.nome}")
        print("==============================")

        if not self.plano.treinos:
            print("Nenhum treino cadastrado.")
            return

        for indice, treino in enumerate(self.plano.treinos, 1):

            print(f"\nTreino {indice}: {treino.descricao()}")
            print(f"Nível: {treino.nivel}")
            print(f"Dificuldade: {treino.calcular_dificuldade()}")
            print(f"Calorias: {treino.calcular_calorias():.2f}")

            if isinstance(treino, TreinoFlexibilidade):
                print(f"Ganho de mobilidade: {treino.calcular_mobilidade():.2f}")

        print("\n------------------------------")
        print(f"Total semanal de calorias: {self.plano.calcular_calorias_semana():.2f}")
        print("------------------------------")
