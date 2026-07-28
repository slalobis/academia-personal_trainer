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

    def quantidade_treinos(self):

        total = 0

        for lista in self.__dias.values():
            total += len(lista)

        return total

    def adicionar_exercicio(self, dia, treino):

        if dia not in self.__dias:

            print("Dia inválido!")
            return False

        if self.quantidade_treinos() >= 5:

            print("Limite de 5 treinos na semana atingido!")
            return False

        self.__dias[dia].append(treino)

        return True

    def calcular_calorias_semana(self):

        total = 0

        for lista in self.__dias.values():

            for treino in lista:

                total += treino.calcular_calorias()

        return total
