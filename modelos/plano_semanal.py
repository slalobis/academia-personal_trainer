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

    def dia_cheio(self, dia):

        if dia not in self.__dias:
            return False

        return len(self.__dias[dia]) >= 5

    def adicionar_exercicio(self, dia, treino):

        if dia not in self.__dias:

            print("Dia inválido!")
            return False

        if self.dia_cheio(dia):

            print(f"{dia} já possui o número máximo de treinos!")
            return False

        self.__dias[dia].append(treino)

        return True

    def calcular_calorias_semana(self):

        total = 0

        for lista in self.__dias.values():

            for treino in lista:

                total += treino.calcular_calorias()

        return total