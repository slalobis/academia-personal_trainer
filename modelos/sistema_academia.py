from modelos.aluno import Aluno
from modelos.instrutor import Instrutor
from modelos.plano_semanal import PlanoSemanal
from modelos.ficha_treino import FichaTreino

from modelos.treino_forca import TreinoForca
from modelos.treino_cardio import TreinoCardio
from modelos.treino_flexibilidade import TreinoFlexibilidade


class SistemaAcademia:

    def __init__(self):

        self.__aluno = None
        self.__instrutor = None
        self.__plano = PlanoSemanal()
        self.__descanso = 0
        self.__ficha = None

        self.__dias = {
            1: "Segunda",
            2: "Terça",
            3: "Quarta",
            4: "Quinta",
            5: "Sexta"
        }

        self.__niveis = {
            1: "Iniciante",
            2: "Intermediário",
            3: "Avançado"
        }

    # ==========================
    # Cadastro do aluno
    # ==========================

    def cadastrar_aluno(self):

        print("=" * 50)
        print("CADASTRO DO ALUNO")
        print("=" * 50)

        nome = input("Nome: ")
        idade = int(input("Idade: "))
        peso = float(input("Peso (kg): "))
        altura = float(input("Altura (m): "))
        objetivo = input("Objetivo: ")
        meses = int(input("Tempo de matrícula (meses): "))

        self.__aluno = Aluno(nome, idade, peso, altura, objetivo, meses)

    # ==========================
    # Cadastro do instrutor
    # ==========================

    def cadastrar_instrutor(self):

        print("\n" + "=" * 50)
        print("CADASTRO DO INSTRUTOR")
        print("=" * 50)

        nome = input("Nome: ")

        self.__instrutor = Instrutor(nome)

        self.__descanso = int(
            input("Tempo de descanso entre séries (segundos): ")
        )

    # ==========================
    # Validação do nível
    # ==========================

    def validar_nivel(self, nivel):

        meses = self.__aluno.meses_matricula

        if meses < 1:
            return nivel == "Iniciante"

        elif meses < 3:
            return nivel != "Avançado"

        return True

    # ==========================
    # Criar treino
    # ==========================

    def criar_treino(self, tipo, nivel):

        if tipo == 1:

            exercicio = input("Exercício: ")
            peso = float(input("Peso (kg): "))
            series = int(input("Séries: "))
            repeticoes = int(input("Repetições: "))

            return TreinoForca(exercicio, peso, series, repeticoes, nivel)

        elif tipo == 2:

            atividade = input("Atividade: ")
            tempo = int(input("Tempo (minutos): "))
            intensidade = input(
                "Intensidade (Leve/Moderada/Intensa): "
            )

            return TreinoCardio(atividade, tempo, intensidade, nivel)

        elif tipo == 3:

            alongamento = input("Alongamento: ")
            tempo = int(input("Tempo (segundos): "))

            return TreinoFlexibilidade(alongamento, tempo, nivel)

        return None

    # ==========================
    # Cadastro dos treinos
    # ==========================

    def cadastrar_treinos(self):

        while True:

            print("\n" + "=" * 50)
            print("CADASTRO DE TREINOS")
            print("=" * 50)

            print("\nEscolha o dia")

            for numero, dia in self.__dias.items():
                print(f"{numero} - {dia}")

            print("0 - Finalizar")

            try:
                op_dia = int(input("Opção: "))
            except ValueError:
                print("Digite apenas números.")
                continue

            if op_dia == 0:
                break

            if op_dia not in self.__dias:
                print("Dia inválido!")
                continue

            dia = self.__dias[op_dia]

            if self.__plano.dia_cheio(dia):

                print(f"\n{dia} já possui o limite de 5 treinos.")
                continue

            print("\nTipo de treino")

            print("1 - Força")
            print("2 - Cardio")
            print("3 - Flexibilidade")

            try:
                tipo = int(input("Escolha: "))
            except ValueError:
                print("Digite apenas números.")
                continue

            print("\nNível")

            for numero, nivel in self.__niveis.items():
                print(f"{numero} - {nivel}")

            try:
                op_nivel = int(input("Escolha: "))
            except ValueError:
                print("Digite apenas números.")
                continue

            if op_nivel not in self.__niveis:
                print("Nível inválido!")
                continue

            nivel = self.__niveis[op_nivel]

            if not self.validar_nivel(nivel):

                print(
                    "\nO aluno ainda não possui tempo de matrícula "
                    "suficiente para esse nível."
                )
                continue

            treino = self.criar_treino(tipo, nivel)

            if treino is None:
                print("Tipo de treino inválido!")
                continue

            if self.__plano.adicionar_exercicio(dia, treino):

                print("\nTreino cadastrado com sucesso!")

    # ==========================
    # Gerar ficha
    # ==========================

    def gerar_ficha(self):

        self.__ficha = FichaTreino(
            self.__aluno,
            self.__instrutor,
            self.__plano,
            self.__descanso
        )

        self.__ficha.mostrar()

    # ==========================
    # Executar sistema
    # ==========================

    def executar(self):

        self.cadastrar_aluno()
        self.cadastrar_instrutor()
        self.cadastrar_treinos()
        self.gerar_ficha()
