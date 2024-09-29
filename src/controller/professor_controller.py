from .entidade_controller import EntidadeController
from utils.valida_cpf import valida_cpf
from utils.constants import INVALID_CODE


class ProfessorController:
    def __init__(self):
        self.entidade = EntidadeController("professores")

    def criar_professor(self):
        codigo = self.entidade.gerar_identificador_unico()
        nome = input("Digite o nome do professor: ")
        cpf = input("Digite o CPF do professor: ")

        if valida_cpf(cpf):
            professor = {"codigo": codigo, "nome": nome, "cpf": cpf}
            self.entidade.criar_entidade(professor)
            print("\nProfessor criado!")

    def ler_professor(self):
        self.entidade.ler_entidade()

    def atualizar_professor(self):
        codigo_de_entrada = input("Digite o código do professor a ser atualizado: ")

        if not self.entidade.validar_codigo_existente(codigo_de_entrada):
            return

        novo_nome = input("Digite o novo nome do professor: ")
        novo_cpf = input("Digite o novo CPF do professor: ")

        if valida_cpf(novo_cpf):
            novos_dados = {"nome": novo_nome, "cpf": novo_cpf}
            self.entidade.atualizar_entidade(codigo_de_entrada, novos_dados)
            print("\nProfessor atualizado!")

    def deletar_professor(self):
        codigo_de_entrada = input("Digite o código do professor a ser deletado: ")

        if not self.entidade.validar_codigo_existente(codigo_de_entrada):
            return

        self.entidade.deletar_entidade(codigo_de_entrada)
        print("\nProfessor deletado!")
