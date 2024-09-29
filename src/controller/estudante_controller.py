from .entidade_controller import EntidadeController
from utils.valida_cpf import valida_cpf
from utils.constants import INVALID_CODE



class EstudanteController:
        def __init__(self):
                self.entidade = EntidadeController("estudantes")

        def criar_estudante(self):
                codigo = self.entidade.gerar_identificador_unico()
                nome = input("Digite o nome do estudante: ")
                cpf = input("Digite o CPF do estudante: ")

                if valida_cpf(cpf):
                        estudante = {"codigo": codigo, "nome": nome, "cpf": cpf}
                        self.entidade.criar_entidade(estudante)
                        print("\nEstudante criado!")

        def ler_estudante(self):
                self.entidade.ler_entidade()

        def atualizar_estudante(self):
                codigo_de_entrada = input("Digite o código do estudante a ser atualizado: ")

                if not self.entidade.validar_codigo_existente(codigo_de_entrada):
                        return

                novo_nome = input("Digite o novo nome do estudante: ")
                novo_cpf = input("Digite o novo CPF do estudante: ")

                if valida_cpf(novo_cpf):
                        novos_dados = {"nome": novo_nome, "cpf": novo_cpf}
                        self.entidade.atualizar_entidade(codigo_de_entrada, novos_dados)
                        print("\nEstudante atualizado!")

        def deletar_estudante(self):
                codigo_de_entrada = input("Digite o código do estudante a ser deletado: ")

                if not self.entidade.validar_codigo_existente(codigo_de_entrada):
                        return

                self.entidade.deletar_entidade(codigo_de_entrada)
                print("\nEstudante deletado!")
