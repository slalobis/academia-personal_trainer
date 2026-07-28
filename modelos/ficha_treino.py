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

                print(f"\nTreino {indice}")
                print()

                print(treino)

                print("-" * 70)

        print("\n" + "=" * 70)

        print(
            f"TOTAL DE CALORIAS QUEIMADAS NA SEMANA: "
            f"{self.__plano.calcular_calorias_semana():.2f} kcal"
        )

        print("=" * 70)
