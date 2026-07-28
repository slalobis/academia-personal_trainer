class Dificuldade:

    def calcular_dificuldade(self):

        dificuldades = {
            "iniciante": "Fácil",
            "intermediario": "Médio",
            "avancado": "Difícil"
        }

        return dificuldades[self.nivel]
