from controller import criar_disciplina, ler_disciplina, atualizar_disciplina, deletar_disciplina

def gerenciar_disciplinas():
  while True:
    print("Gerenciando disciplinas")
    print("1: Criar disciplina")
    print("2: Ler disciplina")
    print("3: Atualizar disciplina")
    print("4: Deletar disciplina")
    print("9: Voltar para o menu principal")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
      criar_disciplina()
    elif opcao == "2":
      ler_disciplina()
    elif opcao == "3":
      atualizar_disciplina()
    elif opcao == "4":
      deletar_disciplina()
    elif opcao == "9":
      break
    else:
      print("Opção inválida. Tente novamente.")