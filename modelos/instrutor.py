class Instrutor:

    def __init__(self, nome):

        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def __str__(self):

        return (
            f"Instrutor: {self.nome}"
        )
