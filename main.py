from modelos.aluno import Aluno
from modelos.plano_semanal import PlanoSemanal
from modelos.treino_forca import TreinoForca
from modelos.treino_cardio import TreinoCardio
from modelos.treino_flexibilidade import TreinoFlexibilidade


def main():
    # -------------------------
    # Cadastro do aluno
    # -------------------------
    aluno = Aluno("Diego", 2)

    print("=" * 40)
    aluno.exibir_dados()
    print("=" * 40)

    # -------------------------
    # Criação do plano semanal
    # -------------------------
    plano = PlanoSemanal()

    # -------------------------
    # Criação dos treinos
    # -------------------------
    treino_forca = TreinoForca(
        duracao=60,
        peso_levantado=80,
        series=4
    )

    treino_cardio = TreinoCardio(
        duracao=30,
        intensidade=6
    )

    treino_flexibilidade = TreinoFlexibilidade(
        duracao=45,
        nivel_alongamento=8
    )

    treinos = [
        treino_forca,
        treino_cardio,
        treino_flexibilidade
    ]

    # -------------------------
    # Verificação dos treinos
    # -------------------------
    print("\nVerificando treinos...\n")

    for treino in treinos:

        if aluno.pode_realizar_treino(treino):

            print(
                f"{treino.__class__.__name__}: Treino permitido."
            )

            plano.adicionar_treino(treino)

            # Apenas TreinoCardio possui monitoramento
            if isinstance(treino, TreinoCardio):
                treino.registrar_execucao(
                    "Treino adicionado ao plano semanal."
                )

        else:

            print(
                f"{treino.__class__.__name__}: Treino NÃO permitido."
            )

    # -------------------------
    # Plano semanal
    # -------------------------
    print("\n")
    plano.listar_treinos()

    print(
        f"Quantidade de treinos: "
        f"{plano.quantidade_treinos()}"
    )

    print(
        f"Total de calorias: "
        f"{plano.calcular_total_calorias():.2f} kcal"
    )

    # -------------------------
    # Histórico do cardio
    # -------------------------
    print("\n")

    treino_cardio.exibir_historico()


if __name__ == "__main__":
    main()
