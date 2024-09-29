from .entidade_controller import EntidadeController
from utils.numero_inteiro import obter_codigo_inteiro


class TurmaController:
    def __init__(self):
        self.entidade = EntidadeController("turmas")

    def criar_turma(self):
        codigo_turma = self.entidade.gerar_identificador_unico()
        codigo_professor = obter_codigo_inteiro("Digite o código do professor: ")
        codigo_disciplina = obter_codigo_inteiro("Digite o código da disciplina: ")

        turma = {
            "codigo": codigo_turma,
            "codigo_professor": codigo_professor,
            "codigo_disciplina": codigo_disciplina,
        }
        self.entidade.criar_entidade(turma)
        print("\nTurma criada!")

    def ler_turma(self):
        self.entidade.ler_entidade()

    def atualizar_turma(self):
        codigo_turma = input("Digite o código da turma a ser atualizada: ")

        if not self.entidade.validar_codigo_existente(codigo_turma):
            print("Erro: Código não encontrado.")
            return

        novo_codigo_professor = obter_codigo_inteiro(
            "Digite o novo código do professor: "
        )
        novo_codigo_disciplina = obter_codigo_inteiro(
            "Digite o novo código da disciplina: "
        )

        novos_dados = {
            "codigo_professor": novo_codigo_professor,
            "codigo_disciplina": novo_codigo_disciplina,
        }
        self.entidade.atualizar_entidade(codigo_turma, novos_dados)
        print("\nTurma atualizada!")

    def deletar_turma(self):
        codigo_turma = input("Digite o código da turma a ser deletada: ")

        if not self.entidade.validar_codigo_existente(codigo_turma):
            print("Erro: Código não encontrado.")
            return

        self.entidade.deletar_entidade(codigo_turma)
        print("\nTurma deletada!")
