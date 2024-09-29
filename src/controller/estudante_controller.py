from .entidade_controller import EntidadeController

entidade = EntidadeController("estudantes")

def criar_estudante():
        codigo = entidade.gerar_identificador_unico()
        nome = input("Digite o nome do estudante: ")
        cpf = input("Digite o CPF do estudante: ")

        estudante = {"codigo": codigo, "nome": nome, "cpf": cpf}
        entidade.criar_entidade("estudantes", estudante)
        print("\nEstudante criado!")

def ler_estudante():
        entidade.ler_entidade("estudantes")

def atualizar_estudante():
        codigo_de_entrada = input("Digite o código do estudante a ser atualizado: ")

        if not entidade.validar_codigo_existente("estudantes", codigo_de_entrada):
                print("Erro: Código não encontrado.")
                return

        novo_nome = input("Digite o novo nome do estudante: ")
        novo_cpf = input("Digite o novo CPF do estudante: ")

        novos_dados = {"nome": novo_nome, "cpf": novo_cpf}
        entidade.atualizar_entidade("estudantes", codigo_de_entrada, novos_dados)
        print("\nEstudante atualizado!")

def deletar_estudante():
        codigo_de_entrada = input("Digite o código do estudante a ser deletado: ")

        if not entidade.validar_codigo_existente("estudantes", codigo_de_entrada):
                print("Erro: Código não encontrado.")
                return

        entidade.deletar_entidade("estudantes", codigo_de_entrada)
        print("\nEstudante deletado!")
