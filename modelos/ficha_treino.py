from modelos.avaliavel import Avaliavel

class FichaTreino:

    def __init__(self,
                 aluno,
                 instrutor,
                 plano,
                 descanso):

        self.__aluno = aluno
        self.__instrutor = instrutor
        self.__plano = plano
        self.__descanso = descanso

    def mostrar(self):
        total_calorias = 0

        print("\n")
        print("=" * 70)
        print(" " * 24 + "FICHA DE TREINO")
        print("=" * 70)

        print(self.__aluno)
        print()

        print(self.__instrutor)
        print()

        print(f"Tempo de descanso: {self.__descanso} segundos")

        print("=" * 70)

        for dia, treinos in self.__plano.dias.items():

            print(f"\n{dia.upper()}")

            if not treinos:
                print("Nenhum treino cadastrado.")
                continue

            print("-" * 70)

            for indice, treino in enumerate(treinos, start=1):

                print(f"\nTreino {indice}\n")
                print(treino)

                if isinstance(treino, Avaliavel):
                    print(f"Recomendação: {treino.recomendacao()}")

                total_calorias += treino.calcular_calorias()

                print("-" * 70)

        print("=" * 70)
        print(f"\nTotal de calorias queimadas na semana: {total_calorias:.2f} kcal\n")