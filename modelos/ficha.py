from plano_semanal import PlanoSemanal

class FichaTreino:

    def __init__(self, aluno, instrutor, objetivo, descanso):
        self.__aluno = aluno
        self.__instrutor = instrutor
        self.__objetivo = objetivo
        self.__descanso = descanso
        self.__plano = PlanoSemanal()

    @property
    def plano(self):
        return self.__plano

    def mostrar(self):

        print("="*60)
        print("                FICHA DE TREINO")
        print("="*60)

        print(f"Aluno: {self.__aluno.nome}")
        print(f"Instrutor: {self.__instrutor.nome}")
        print(f"CREF: {self.__instrutor.cref}")
        print(f"Objetivo: {self.__objetivo}")
        print(f"Descanso: {self.__descanso} segundos\n")

        for dia, exercicios in self.__plano.dias.items():

            print("-"*60)
            print(dia.upper())
            print("-"*60)

            if not exercicios:
                print("Nenhum exercício cadastrado.\n")
                continue

            for i, treino in enumerate(exercicios, 1):

                print(f"{i}. {treino.exercicio}")
                print(f"   Séries: {treino.series}")
                print(f"   Repetições: {treino.vezes_levantado}")
                print(f"   Peso: {treino.peso_levantado} kg\n")
