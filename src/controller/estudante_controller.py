estudantesArray = []

def criar_estudante():
    codigo = int(input("Digite o código do estudante: "))
    nome = input("Digite o nome do estudante: ")
    cpf = input("Digite o CPF do estudante: ")
    estudante = {
      "codigo": codigo,
      "nome": nome,
      "cpf": cpf
    }
    estudantesArray.append(estudante)
    print("\nEstudante criado!")

def ler_estudante():
    if not estudantesArray:
        print("\nNão há estudantes cadastrados")
    else:
        print("\nLista de estudantes:")
        for estudante in estudantesArray:
            print(f"Código: {estudante['codigo']}, Nome: {estudante['nome']}, CPF: {estudante['cpf']}")

def atualizar_estudante():
    codigo_de_entrada = int(input("Digite o código do estudante a ser atualizado: "))
    for estudante in estudantesArray:
        if estudante['codigo'] == codigo_de_entrada:
            novo_codigo = int(input("Digite o novo código do estudante: "))
            novo_nome = input("Digite o novo nome do estudante: ")
            nove_cpf = input("Digite o novo CPF do estudante: ")
            estudante['codigo'] = novo_codigo
            estudante['nome'] = novo_nome
            estudante['cpf'] = nove_cpf
            print("\nEstudante atualizado!")
            return
    print("\nEstudante não encontrado!")

def deletar_estudante():
    codigo_de_entrada = int(input("Digite o código do estudante a ser deletado: "))
    for estudante in estudantesArray:
        if estudante['codigo'] == codigo_de_entrada:
            estudantesArray.remove(estudante)
            print("\nEstudante deletado!")
            return
    print("\nEstudante não encontrado!")