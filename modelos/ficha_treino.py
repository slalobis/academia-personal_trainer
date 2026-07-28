from plano_semanal import PlanoSemanal

class FichaTreino:

    def __init__(self,
                 aluno,
                 instrutor,
                 descanso):

        self.__aluno = aluno
        self.__instrutor = instrutor
        self.__descanso = descanso

        self.__plano = PlanoSemanal()

    @property
    def plano(self):
        return self.__plano

    def mostrar(self):

        print("="*70)
        print("                    FICHA DE TREINO")
        print("="*70)

        print(f"Aluno: {self.__aluno.nome}")
        print(f"Idade: {self.__aluno.idade}")
        print(f"Peso: {self.__aluno.peso} kg")
        print(f"Altura: {self.__aluno.altura} m")
        print(f"Objetivo: {self.__aluno.objetivo}")

        print()

        print(f"Instrutor: {self.__instrutor.nome}")
        print(f"CREF: {self.__instrutor.cref}")

        print()

        print(f"Tempo de descanso: {self.__descanso} segundos")

        print()

        for dia, exercicios in self.__plano.dias.items():

            print("-"*70)
            print(dia.upper())
            print("-"*70)

            if len(exercicios) == 0:
                print("Nenhum exercício cadastrado.\n")
                continue

            for i, treino in enumerate(exercicios,1):

                print(f"{i}. {treino.exercicio}")
                print(f"   Nível: {treino.nivel}")
                print(f"   Dificuldade: {treino.dificuldade.value}")
                print(f"   Séries: {treino.series}")
                print(f"   Repetições: {treino.repeticoes}")
                print(f"   Peso: {treino.peso} kg")
                print()
