def exibir_menu(titulo, opcoes):
    print(f"\n\n***** [{titulo}] MENU DE OPERAÇÕES *****\n")
    for chave, valor in opcoes.items():
        print(f'({chave}) {valor}.')
    print('(9) Voltar ao menu principal.\n')
    try:
        acao = int(input('Informe a ação desejada: '))
    except ValueError:
        print("\n\nOpção incorreta!")
        return None
    return acao
