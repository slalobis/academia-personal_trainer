class Aluno:

    def __init__(self, nome, idade, peso, altura, objetivo, meses_matricula):

        self.__nome = nome
        self.__idade = idade
        self.__peso = peso
        self.__altura = altura
        self.__objetivo = objetivo
        self.__meses_matricula = meses_matricula

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade

    @property
    def peso(self):
        return self.__peso

    @property
    def altura(self):
        return self.__altura

    @property
    def objetivo(self):
        return self.__objetivo

    @property
    def meses_matricula(self):
        return self.__meses_matricula

    def __str__(self):

        return (
            f"Aluno: {self.nome}\n"
            f"Idade: {self.idade}\n"
            f"Peso: {self.peso} kg\n"
            f"Altura: {self.altura} m\n"
            f"Objetivo: {self.objetivo}\n"
            f"Tempo de matrícula: {self.meses_matricula} meses"
        )
