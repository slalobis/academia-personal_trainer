class PlanoSemanal:

    def __init__(self):

        self.__dias = {
            "Segunda": [],
            "Terça": [],
            "Quarta": [],
            "Quinta": [],
            "Sexta": []
        }

    @property
    def dias(self):
        return self.__dias

    def adicionar_exercicio(self, dia, treino):

        if dia in self.__dias:
            self.__dias[dia].append(treino)
        else:
            print("Dia inválido.")
