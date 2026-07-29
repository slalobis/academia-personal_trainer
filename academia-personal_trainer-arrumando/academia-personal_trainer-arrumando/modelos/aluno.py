from modelos.plano_semanal import PlanoSemanal


class Aluno:
    """
    Classe que representa um aluno da academia.
    """

    def __init__(self, nome, meses_matricula):
        self.nome = nome
        self.meses_matricula = meses_matricula
        self.__plano_semanal = PlanoSemanal()

    # -------------------------
    # Encapsulamento
    # -------------------------

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        if not valor.strip():
            raise ValueError("O nome não pode ser vazio.")
        self.__nome = valor

    @property
    def meses_matricula(self):
        return self.__meses_matricula

    @meses_matricula.setter
    def meses_matricula(self, valor):
        if valor < 0:
            raise ValueError("Os meses de matrícula não podem ser negativos.")
        self.__meses_matricula = valor

    @property
    def plano_semanal(self):
        return self.__plano_semanal

    # -------------------------
    # Regras de negócio
    # -------------------------

    def pode_realizar_treino(self, treino):
        """
        Verifica se o aluno pode realizar determinado treino.
        """

        if (
            self.meses_matricula < 1
            and treino.nivel_dificuldade() == "Avançado"
        ):
            return False

        return True

    # -------------------------
    # Método auxiliar
    # -------------------------

    def exibir_dados(self):
        print("=== Aluno ===")
        print(f"Nome: {self.nome}")
        print(f"Meses de matrícula: {self.meses_matricula}")