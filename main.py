from aluno import Aluno
from instrutor import Instrutor
from treino_forca import TreinoForca
from dificuldade import Dificuldade
from ficha_treino import FichaTreino

# Cadastro do aluno

nome = input("Nome do aluno: ")
idade = int(input("Idade: "))
peso = float(input("Peso: "))
altura = float(input("Altura: "))
objetivo = input("Objetivo: ")

aluno = Aluno(
    nome,
    idade,
    peso,
    altura,
    objetivo
)

# Cadastro do instrutor

nome_instrutor = input("Nome do instrutor: ")
cref = input("CREF: ")

instrutor = Instrutor(
    nome_instrutor,
    cref
)

descanso = int(input("Tempo de descanso (segundos): "))

ficha = FichaTreino(
    aluno,
    instrutor,
    descanso
)

while True:

    print("\nDias disponíveis")
    print("Segunda")
    print("Terça")
    print("Quarta")
    print("Quinta")
    print("Sexta")

    dia = input("\nDia do treino (ou fim): ")

    if dia.lower() == "fim":
        break

    exercicio = input("Exercício: ")

    series = int(input("Séries: "))
    repeticoes = int(input("Repetições: "))
    peso = float(input("Peso (kg): "))

    nivel = input("Nível (Iniciante/Intermediário/Avançado): ")

    print("\nDificuldade")
    print("1 - Fácil")
    print("2 - Média")
    print("3 - Difícil")

    op = int(input("Escolha: "))

    if op == 1:
        dificuldade = Dificuldade.FACIL
    elif op == 2:
        dificuldade = Dificuldade.MEDIA
    else:
        dificuldade = Dificuldade.DIFICIL

    treino = TreinoForca(
        exercicio,
        peso,
        series,
        repeticoes,
        nivel,
        dificuldade
    )

    ficha.plano.adicionar_exercicio(
        dia,
        treino
    )

print()

ficha.mostrar()
