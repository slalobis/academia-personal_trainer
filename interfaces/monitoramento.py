from datetime import datetime


class Monitoramento:
    """
    Classe responsável por registrar informações sobre a execução
    dos treinos.
    """

    def __init__(self):
        self._historico = []

    @property
    def historico(self):
        return self._historico

    def registrar_execucao(self, mensagem):
        """
        Registra um evento no histórico do treino.
        """
        horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        registro = f"[{horario}] {mensagem}"
        self._historico.append(registro)

    def exibir_historico(self):
        """
        Exibe todos os registros armazenados.
        """
        if not self._historico:
            print("Nenhum registro encontrado.")
            return

        print("\n=== Histórico ===")

        for registro in self._historico:
            print(registro)
