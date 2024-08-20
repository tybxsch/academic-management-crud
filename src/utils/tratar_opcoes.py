def tratar_opcao(acao, modulo):
    if acao == 1:
        modulo.cadastrar()
    elif acao == 2:
        modulo.listar()
    elif acao == 3:
        modulo.atualizar()
    elif acao == 4:
        modulo.excluir()
    elif acao == 9:
        # TODO: A volta para o menu principal não está funcionando corretamente
        try:
            from src.main import menu_principal
            menu_principal()
        except ImportError as e:
            print(f"Erro ao importar menu_principal: {e}")
    else:
        print("\n\nOpção incorreta!")