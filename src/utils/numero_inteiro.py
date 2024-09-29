def obter_codigo_inteiro(mensagem):
    while True:
        try:
            codigo = int(input(mensagem))
            return codigo
        except ValueError:
            print("Erro: Por favor, digite um número inteiro.")
