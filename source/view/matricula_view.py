from controller import criar_matricula, ler_matricula, atualizar_matricula, deletar_matricula

def gerenciar_matriculas():
  while True:
    print("Gerenciando matriculas")
    print("1: Criar matricula")
    print("2: Ler matricula")
    print("3: Atualizar matricula")
    print("4: Deletar matricula")
    print("9: Voltar para o menu principal")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
      criar_matricula()
    elif opcao == "2":
      ler_matricula()
    elif opcao == "3":
      atualizar_matricula()
    elif opcao == "4":
      deletar_matricula()
    elif opcao == "9":
      break
    else:
      print("Opção inválida. Tente novamente.")