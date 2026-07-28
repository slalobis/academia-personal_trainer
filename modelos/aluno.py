class Aluno:

    def __init__(self,
                 nome,
                 idade,
                 peso,
                 altura,
                 objetivo):

        self.__nome = nome
        self.__idade = idade
        self.__peso = peso
        self.__altura = altura
        self.__objetivo = objetivo

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
