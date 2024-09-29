from .entidade_controller import EntidadeController
from utils.numero_inteiro import obter_codigo_inteiro
from utils.constants import INVALID_CODE


class MatriculaController:
    def __init__(self):
        self.entidade = EntidadeController("matriculas")

    def criar_matricula(self):
        codigo_matricula = self.entidade.gerar_identificador_unico()
        codigo_turma = obter_codigo_inteiro("Digite o código da turma: ")
        codigo_estudante = obter_codigo_inteiro("Digite o código do estudante: ")

        matricula = {
            "codigo": codigo_matricula,
            "codigo_turma": codigo_turma,
            "codigo_estudante": codigo_estudante,
        }
        self.entidade.criar_entidade(matricula)
        print("\nMatrícula criada!")

    def ler_matricula(self):
        self.entidade.ler_entidade()

    def atualizar_matricula(self):
        codigo_matricula = input("Digite o código da matrícula a ser atualizada: ")

        if not self.entidade.validar_codigo_existente(codigo_matricula):
            return

        novo_codigo_turma = obter_codigo_inteiro("Digite o novo código da turma: ")
        novo_codigo_estudante = obter_codigo_inteiro(
            "Digite o novo código do estudante: "
        )

        novos_dados = {
            "codigo_turma": novo_codigo_turma,
            "codigo_estudante": novo_codigo_estudante,
        }
        self.entidade.atualizar_entidade(codigo_matricula, novos_dados)
        print("\nMatrícula atualizada!")

    def deletar_matricula(self):
        codigo_matricula = input("Digite o código da matrícula a ser deletada: ")

        if not self.entidade.validar_codigo_existente(codigo_matricula):
            return

        self.entidade.deletar_entidade(codigo_matricula)
        print("\nMatrícula deletada!")
