import re

estudantesArray = []


def validar_codigo(codigo):
    return any(estudante["codigo"] == codigo for estudante in estudantesArray)


def validar_cpf(cpf):
    cpf = re.sub(r"\D", "", cpf)
    return len(cpf) == 11


def encontrar_estudante_por_codigo(codigo):
    for estudante in estudantesArray:
        if estudante["codigo"] == codigo:
            return estudante
    return None


def criar_estudante():
    while True:
        try:
            codigo = int(input("Digite o código do estudante: "))
            if validar_codigo(codigo):
                print("Código já existe. Por favor, digite um código diferente.")
            else:
                break
        except ValueError:
            print("Código inválido. Por favor, digite um número inteiro.")

    nome = input("Digite o nome do estudante: ")

    while True:
        cpf = input("Digite o CPF do estudante (11 caracteres): ")
        if validar_cpf(cpf):
            cpf = re.sub(r"\D", "", cpf)
            break
        else:
            print("CPF inválido. Deve conter exatamente 11 caracteres.")

    estudante = {"codigo": codigo, "nome": nome, "cpf": cpf}
    estudantesArray.append(estudante)
    print("\nEstudante criado!")


def ler_estudante():
    if not estudantesArray:
        print("\nNão há estudantes cadastrados")
    else:
        print("\nLista de estudantes:")
        for estudante in estudantesArray:
            print(
                f"Código: {estudante['codigo']}, Nome: {estudante['nome']}, CPF: {estudante['cpf']}"
            )


def atualizar_estudante():
    try:
        codigo_de_entrada = int(
            input("Digite o código do estudante a ser atualizado: ")
        )
    except ValueError:
        print("Código inválido. Por favor, digite um número inteiro.")
        return

    estudante = encontrar_estudante_por_codigo(codigo_de_entrada)
    if estudante:
        while True:
            try:
                novo_codigo = int(input("Digite o novo código do estudante: "))
                if validar_codigo(novo_codigo) and novo_codigo != estudante["codigo"]:
                    print("Código já existe. Por favor, digite um código diferente.")
                else:
                    break
            except ValueError:
                print("Código inválido. Por favor, digite um número inteiro.")

        novo_nome = input("Digite o novo nome do estudante: ")

        while True:
            novo_cpf = input("Digite o novo CPF do estudante (11 caracteres): ")
            if validar_cpf(novo_cpf):
                novo_cpf = re.sub(r"\D", "", novo_cpf)
                break
            else:
                print("CPF inválido. Deve conter exatamente 11 caracteres.")

        estudante["codigo"] = novo_codigo
        estudante["nome"] = novo_nome
        estudante["cpf"] = novo_cpf
        print("\nEstudante atualizado!")
    else:
        print("\nEstudante não encontrado!")


def deletar_estudante():
    try:
        codigo_de_entrada = int(input("Digite o código do estudante a ser deletado: "))
    except ValueError:
        print("Código inválido. Por favor, digite um número inteiro.")
        return

    estudante = encontrar_estudante_por_codigo(codigo_de_entrada)
    if estudante:
        estudantesArray.remove(estudante)
        print("\nEstudante deletado!")
    else:
        print("\nEstudante não encontrado!")
