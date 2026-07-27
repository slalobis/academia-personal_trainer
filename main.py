from modelos.aluno import Aluno

from modelos.treino_forca import TreinoForca
from modelos.treino_cardio import TreinoCardio
from modelos.treino_flexibilidade import TreinoFlexibilidade

diego = Aluno("Diego", 0)
pedro = Aluno("Pedro", 1.5)
ana = Aluno("Ana", 3)

# Treinos

forca_iniciante = TreinoForca(50, 3, "iniciante")
cardio_iniciante = TreinoCardio(30, 5, "iniciante")
flexibilidade_iniciante = TreinoFlexibilidade(40, "iniciante")

forca_intermediario = TreinoForca(80, 5, "intermediario")
cardio_intermediario = TreinoCardio(45, 7, "intermediario")
flexibilidade_intermediario = TreinoFlexibilidade(60, "intermediario")

forca_avancado = TreinoForca(100, 8, "avancado")
cardio_avancado = TreinoCardio(60, 10, "avancado")
flexibilidade_avancado = TreinoFlexibilidade(90, "avancado")

# ==========================
# Diego
# ==========================

diego.adicionar_treino(forca_iniciante)
diego.adicionar_treino(cardio_iniciante)
diego.adicionar_treino(forca_intermediario)      # Bloqueado (Diego tem menos de 1 mês de treino)
diego.adicionar_treino(cardio_avancado)          # Bloqueado (Diego tem menos de 3 meses de treino)
diego.adicionar_treino(flexibilidade_iniciante)
diego.adicionar_treino(flexibilidade_avancado)   # Bloqueado (Diego tem menos de 3 meses de treino)

diego.mostrar_plano()

# ==========================
# Pedro
# ==========================

pedro.adicionar_treino(forca_intermediario)
pedro.adicionar_treino(cardio_intermediario)
pedro.adicionar_treino(flexibilidade_intermediario)      
pedro.adicionar_treino(forca_avancado)               # Bloqueado (Pedro tem menos de 3 meses de treino)
pedro.adicionar_treino(flexibilidade_avancado)       # Bloqueado (Pedro tem menos de 3 meses de treino)
pedro.adicionar_treino(cardio_avancado)              # Bloqueado (Pedro tem menos de 3 meses de treino)

pedro.mostrar_plano()

# ==========================
# Ana
# ==========================

ana.adicionar_treino(forca_intermediario)
ana.adicionar_treino(forca_avancado)
ana.adicionar_treino(cardio_intermediario)
ana.adicionar_treino(cardio_avancado)
ana.adicionar_treino(flexibilidade_intermediario)
ana.adicionar_treino(flexibilidade_avancado)       # Excede o limite semanal (6º treino)

ana.mostrar_plano()
