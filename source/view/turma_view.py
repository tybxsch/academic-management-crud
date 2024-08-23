from controller import criar_turma, ler_turma, atualizar_turma, deletar_turma

def gerenciar_turmas():
  while True:
    print("Gerenciando turmas")
    print("1: Criar turma")
    print("2: Ler turma")
    print("3: Atualizar turma")
    print("4: Deletar turma")
    print("9: Voltar para o menu principal")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
      criar_turma()
    elif opcao == "2":
      ler_turma()
    elif opcao == "3":
      atualizar_turma()
    elif opcao == "4":
      deletar_turma()
    elif opcao == "9":
      break
    else:
      print("Opção inválida. Tente novamente.")