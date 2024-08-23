from view import gerenciar_estudantes, gerenciar_professores, gerenciar_disciplinas, gerenciar_turmas, gerenciar_matriculas

def menu_principal():
  while True:
    print("Menu Principal")
    print("1: Gerenciar estudantes")
    print("2: Gerenciar professores")
    print("3: Gerenciar disciplinas")
    print("4: Gerenciar turmas")
    print("5: Gerenciar matrículas")
    print("9: Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
      gerenciar_estudantes()
    elif opcao == "2":
      gerenciar_professores()
    elif opcao == "3":
      gerenciar_disciplinas()
    elif opcao == "4":
      gerenciar_turmas()
    elif opcao == "5":
      gerenciar_matriculas()
    elif opcao == "9":
      break
    else:
      print("Opção inválida. Tente novamente.")

menu_principal()