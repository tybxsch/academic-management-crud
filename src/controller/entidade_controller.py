from utils.arquivos.ler_json import ler_json
from utils.arquivos.escrever_json import escrever_json


class EntidadeController:
    def __init__(self, nome_entidade):
        self.nome_entidade = nome_entidade
        self.entidades = ler_json(nome_entidade)

    def escrever_json(self):
        escrever_json(self.entidades, self.nome_entidade)

    def gerar_identificador_unico(self):
        if not self.entidades:
            return 1
        return max(entidade["codigo"] for entidade in self.entidades) + 1

    def validar_codigo_existente(self, codigo):
        return any(entidade["codigo"] == codigo for entidade in self.entidades)

    def criar_entidade(self, entidade):
        self.entidades.append(entidade)
        self.escrever_json()

    def ler_entidade(self):
        if not self.entidades:
            print("\nNão há entidades cadastradas")
        else:
            print("\nLista de entidades:")
            for entidade in self.entidades:
                print(entidade)

    def atualizar_entidade(self, codigo, novos_dados):
        for entidade in self.entidades:
            if entidade["codigo"] == codigo:
                entidade.update(novos_dados)
                self.escrever_json()
                return
        print("Erro: Código não encontrado.")

    def deletar_entidade(self, codigo):
        for entidade in self.entidades:
            if entidade["codigo"] == codigo:
                self.entidades.remove(entidade)
                self.escrever_json()
                return
        print("Erro: Código não encontrado.")


# Exemplo de uso para a entidade Estudante
sistema = EntidadeController("estudantes")


def criar_estudante():
    codigo = sistema.gerar_identificador_unico()
    nome = input("Digite o nome do estudante: ")
    cpf = input("Digite o CPF do estudante: ")

    estudante = {"codigo": codigo, "nome": nome, "cpf": cpf}
    sistema.criar_entidade(estudante)
    print("\nEstudante criado!")


def ler_estudante():
    sistema.ler_entidade()


def atualizar_estudante():
    try:
        codigo_de_entrada = int(
            input("Digite o código do estudante a ser atualizado: ")
        )
    except ValueError:
        print("Código inválido. Por favor, digite um número inteiro.")
        return

    if not sistema.validar_codigo_existente(codigo_de_entrada):
        print("Erro: Código não encontrado.")
        return

    novo_nome = input("Digite o novo nome do estudante: ")
    novo_cpf = input("Digite o novo CPF do estudante: ")

    novos_dados = {"nome": novo_nome, "cpf": novo_cpf}
    sistema.atualizar_entidade(codigo_de_entrada, novos_dados)
    print("\nEstudante atualizado!")


def deletar_estudante():
    try:
        codigo_de_entrada = int(input("Digite o código do estudante a ser deletado: "))
    except ValueError:
        print("Código inválido. Por favor, digite um número inteiro.")
        return

    if not sistema.validar_codigo_existente(codigo_de_entrada):
        print("Erro: Código não encontrado.")
        return

    sistema.deletar_entidade(codigo_de_entrada)
    print("\nEstudante deletado!")
