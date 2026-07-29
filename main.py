from modelos.aluno import Aluno
from modelos.treino_forca import TreinoForca
from modelos.treino_cardio import TreinoCardio
from modelos.treino_flexibilidade import TreinoFlexibilidade


def main():

    # ==========================================
    # Cadastro dos alunos
    # ==========================================

    alunos = [
        Aluno("João Pedro", 12),
        Aluno("Diego", 0),
        Aluno("João Vitor", 5),
        Aluno("Guilherme", 2)
    ]

    # ==========================================
    # João Pedro
    # ==========================================

    joao_pedro = alunos[0]

    treinos_joao_pedro = [
        TreinoForca(
            duracao=60,
            peso_levantado=90,
            series=5
        ),

        TreinoCardio(
            duracao=30,
            intensidade=5
        ),

        TreinoFlexibilidade(
            duracao=40,
            nivel_alongamento=7
        )
    ]

    for treino in treinos_joao_pedro:

        if joao_pedro.pode_realizar_treino(treino):

            joao_pedro.plano_semanal.adicionar_treino(treino)

            treino.registrar_execucao(
                f"Treino realizado por {joao_pedro.nome}."
            )

        else:

            print(
                f"\n{joao_pedro.nome} NÃO pode realizar "
                f"{treino.__class__.__name__}"
                f" ({treino.nivel_dificuldade()})."
            )

    # ==========================================
    # Diego
    # ==========================================

    diego = alunos[1]

    treinos_diego = [

        TreinoForca(
            duracao=40,
            peso_levantado=20,
            series=3
        ),

        TreinoCardio(
            duracao=20,
            intensidade=2
        ),

        # Este treino será recusado
        TreinoFlexibilidade(
            duracao=50,
            nivel_alongamento=9
        )
    ]

    for treino in treinos_diego:

        if diego.pode_realizar_treino(treino):

            diego.plano_semanal.adicionar_treino(treino)

            treino.registrar_execucao(
                f"Treino realizado por {diego.nome}."
            )

        else:

            print(
                f"\n{diego.nome} NÃO pode realizar "
                f"{treino.__class__.__name__}"
                f" ({treino.nivel_dificuldade()})."
            )

    # ==========================================
    # João Vitor
    # ==========================================

    joao_vitor = alunos[2]

    treinos_joao_vitor = [

        TreinoForca(
            duracao=50,
            peso_levantado=50,
            series=4
        ),

        TreinoCardio(
            duracao=45,
            intensidade=9
        ),

        TreinoFlexibilidade(
            duracao=30,
            nivel_alongamento=3
        )
    ]

    for treino in treinos_joao_vitor:

        if joao_vitor.pode_realizar_treino(treino):

            joao_vitor.plano_semanal.adicionar_treino(treino)

            treino.registrar_execucao(
                f"Treino realizado por {joao_vitor.nome}."
            )
        else:

            print(
                f"\n{joao_vitor.nome} NÃO pode realizar "
                f"{treino.__class__.__name__}"
                f" ({treino.nivel_dificuldade()})."
            )

    guilherme = alunos[3]
    
    treinos_guilherme = [
    
        TreinoForca(
            duracao=60,
            peso_levantado=20,
            series=2
        ),
    
        TreinoCardio(
            duracao=25,
            intensidade=5
        ),
    
        TreinoFlexibilidade(
            duracao=15,
            nivel_alongamento=1
        )
    ]
    
    for treino in treinos_guilherme:
    
        if guilherme.pode_realizar_treino(treino):
    
            guilherme.plano_semanal.adicionar_treino(treino)
    
            treino.registrar_execucao(
                    f"Treino realizado por {guilherme.nome}."
                )
        else:
    
            print(
                f"\n{guilherme.nome} NÃO pode realizar "
                f"{treino.__class__.__name__}"
                f" ({treino.nivel_dificuldade()})."
            )
    

    # ==========================================
    # Relatório dos alunos
    # ==========================================

    print("\n")
    print("=" * 50)
    print("RELATÓRIO DOS ALUNOS")
    print("=" * 50)

    for aluno in alunos:

        print()

        aluno.exibir_dados()

        print()

        aluno.plano_semanal.listar_treinos()

        print(
            f"Quantidade de treinos: "
            f"{aluno.plano_semanal.quantidade_treinos()}"
        )

        print(
            f"Total de calorias: "
            f"{aluno.plano_semanal.calcular_total_calorias():.2f} kcal"
        )

        print("-" * 50)

    # ==========================================
    # Histórico de todos os treinos
    # ==========================================

    print("\n")
    print("=" * 50)
    print("HISTÓRICO DOS TREINOS")
    print("=" * 50)

    for aluno in alunos:

        print(f"\nAluno: {aluno.nome}")

        for treino in aluno.plano_semanal.treinos:

            print(
                f"\n{treino.__class__.__name__}"
                f" ({treino.nivel_dificuldade()})"
            )

            treino.exibir_historico()


if __name__ == "__main__":
    main()