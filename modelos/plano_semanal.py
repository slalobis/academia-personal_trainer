class PlanoSemanal:
    """
    Classe responsável por armazenar os treinos de um aluno
    durante uma semana.
    """

    def __init__(self):
        self.__treinos = []

    # -------------------------
    # Encapsulamento
    # -------------------------

    @property
    def treinos(self):
        return self.__treinos

    # -------------------------
    # Métodos
    # -------------------------

    def adicionar_treino(self, treino):
        """
        Adiciona um treino ao plano semanal.
        """
        self.__treinos.append(treino)

    def listar_treinos(self):
        """
        Exibe todos os treinos cadastrados.
        """
        if not self.__treinos:
            print("Nenhum treino cadastrado.")
            return

        print("=== Plano Semanal ===")

        for indice, treino in enumerate(self.__treinos, start=1):
            print(f"{indice}. {treino.__class__.__name__}")
            print(f"   Duração: {treino.duracao} minutos")
            print(f"   Dificuldade: {treino.nivel_dificuldade()}")
            print(f"   Calorias: {treino.calcular_calorias():.2f} kcal\n")

    def calcular_total_calorias(self):
        """
        Calcula o total de calorias gastas na semana.
        """
        total = 0

        for treino in self.__treinos:
            total += treino.calcular_calorias()

        return total

    def quantidade_treinos(self):
        """
        Retorna a quantidade de treinos cadastrados.
        """
        return len(self.__treinos)
