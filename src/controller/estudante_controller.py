from utils.arquivos.ler_json import ler_json
from utils.arquivos.escrever_json import escrever_json

ARQUIVO_ESTUDANTES = "estudantes"

def validar_codigo(codigo):
    estudantes = ler_json(ARQUIVO_ESTUDANTES)
    return any(estudante["codigo"] == codigo for estudante in estudantes)

def encontrar_estudante_por_codigo(codigo):
    estudantes = ler_json(ARQUIVO_ESTUDANTES)
    for estudante in estudantes:
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

    cpf = input("Digite o CPF do estudante: ")

    estudante = {"codigo": codigo, "nome": nome, "cpf": cpf}
    estudantes = ler_json(ARQUIVO_ESTUDANTES)
    estudantes.append(estudante)
    escrever_json(estudantes, ARQUIVO_ESTUDANTES)
    print("\nEstudante criado!")

def ler_estudante():
    estudantes = ler_json(ARQUIVO_ESTUDANTES)
    if not estudantes:
        print("\nNão há estudantes cadastrados")
    else:
        print("\nLista de estudantes:")
        for estudante in estudantes:
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

    estudantes = ler_json(ARQUIVO_ESTUDANTES)
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

        novo_cpf = input("Digite o novo CPF do estudante: ")

        for est in estudantes:
            if est["codigo"] == codigo_de_entrada:
                est["codigo"] = novo_codigo
                est["nome"] = novo_nome
                est["cpf"] = novo_cpf
                break

        escrever_json(estudantes, ARQUIVO_ESTUDANTES)
        print("\nEstudante atualizado!")
    else:
        print("\nEstudante não encontrado!")

def deletar_estudante():
    try:
        codigo_de_entrada = int(input("Digite o código do estudante a ser deletado: "))
    except ValueError:
        print("Código inválido. Por favor, digite um número inteiro.")
        return

    estudantes = ler_json(ARQUIVO_ESTUDANTES)
    estudante = encontrar_estudante_por_codigo(codigo_de_entrada)
    if estudante:
        estudantes.remove(estudante)
        escrever_json(estudantes, ARQUIVO_ESTUDANTES)
        print("\nEstudante deletado!")
    else:
        print("\nEstudante não encontrado!")