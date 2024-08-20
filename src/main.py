from views import menu_estudantes, menu_professores, menu_disciplinas, menu_turmas, menu_matriculas

def menu_principal():
    print('----- MENU PRINCIPAL -----\n')
    print('(1) Gerenciar estudantes.')
    print('(2) Gerenciar professores.')
    print('(3) Gerenciar disciplinas.')
    print('(4) Gerenciar turmas.')
    print('(5) Gerenciar matrículas.')
    print('(9) Sair.\n')
    try:
        op = int(input('Informe a opção desejada: '))
    except ValueError:
        print("\n\nOpção incorreta!")
        return menu_principal()

    if op == 1:
        menu_estudantes()
    elif op == 2:
        menu_professores()
    elif op == 3:
        menu_disciplinas()
    elif op == 4:
        menu_turmas()
    elif op == 5:
        menu_matriculas()
    elif op == 9:
        print("Finalizando aplicação...")
    else:
        print("\n\nOpção incorreta!")
        menu_principal()

menu_principal()