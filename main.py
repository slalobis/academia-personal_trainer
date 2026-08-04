from modelos import Aluno, TreinoForca, TreinoCardio, TreinoFlexibilidade

def main():

    # ==========================================
    # Cadastro dos alunos
    # ==========================================

    alunos = [
        Aluno("João Pedro", 12),
        Aluno("Diego", 0),
        Aluno("João Vitor", 5),
        Aluno("Guilherme", 2),
        Aluno("Pedro", 15)
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

        TreinoFlexibilidade(
            duracao=50,
            nivel_alongamento=9
        )
    ]

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

    # ==========================================
    # Guilherme
    # ==========================================

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

    # ==========================================
    # Pedro
    # ==========================================

    pedro = alunos[4]

    treinos_pedro = [

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

    # ==========================================
    # Executando os treinos
    # ==========================================

    joao_pedro.realizar_treinos(treinos_joao_pedro)

    diego.realizar_treinos(treinos_diego)

    joao_vitor.realizar_treinos(treinos_joao_vitor)

    guilherme.realizar_treinos(treinos_guilherme)

    pedro.realizar_treinos(treinos_pedro)

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

    # ==========================================
    # Total de calorias da academia na semana
    # ==========================================

    total_academia = 0

    for aluno in alunos:
        total_academia += aluno.plano_semanal.calcular_total_calorias()

    print("\n")
    print("=" * 50)
    print("TOTAL DE CALORIAS DA ACADEMIA")
    print("=" * 50)
    print(
        f"\nCalorias gastas por todos os alunos: {total_academia:.2f} kcal\n"
    )

if __name__ == "__main__":
    main()
