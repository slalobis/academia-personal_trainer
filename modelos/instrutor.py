class Instrutor:

    def __init__(self,
                 nome,
                 cref):

        self.__nome = nome
        self.__cref = cref

    @property
    def nome(self):
        return self.__nome

    @property
    def cref(self):
        return self.__cref

    def __str__(self):

        return (
            f"Instrutor: {self.nome}\n"
            f"CREF: {self.cref}"
        )
