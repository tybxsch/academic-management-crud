from .entidade_controller import EntidadeController


class DisciplinaController:
    def __init__(self):
        self.entidade = EntidadeController("disciplinas")

    def criar_disciplina(self):
        codigo = self.entidade.gerar_identificador_unico()
        nome = input("Digite o nome da disciplina: ")

        disciplina = {"codigo": codigo, "nome": nome}
        self.entidade.criar_entidade(disciplina)
        print("\nDisciplina criada!")

    def ler_disciplina(self):
        self.entidade.ler_entidade()

    def atualizar_disciplina(self):
        codigo_de_entrada = input("Digite o código da disciplina a ser atualizada: ")

        if not self.entidade.validar_codigo_existente(codigo_de_entrada):
            print("Erro: Código não encontrado.")
            return

        novo_nome = input("Digite o novo nome da disciplina: ")

        novos_dados = {"nome": novo_nome}
        self.entidade.atualizar_entidade(codigo_de_entrada, novos_dados)
        print("\nDisciplina atualizada!")

    def deletar_disciplina(self):
        codigo_de_entrada = input("Digite o código da disciplina a ser deletada: ")

        if not self.entidade.validar_codigo_existente(codigo_de_entrada):
            print("Erro: Código não encontrado.")
            return

        self.entidade.deletar_entidade(codigo_de_entrada)
        print("\nDisciplina deletada!")
