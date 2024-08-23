from controller import criar_professor, ler_professor, atualizar_professor, deletar_professor

def gerenciar_professores():
  while True:
    print("Gerenciando professors")
    print("1: Criar professor")
    print("2: Ler professor")
    print("3: Atualizar professor")
    print("4: Deletar professor")
    print("9: Voltar para o menu principal")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
      criar_professor()
    elif opcao == "2":
      ler_professor()
    elif opcao == "3":
      atualizar_professor()
    elif opcao == "4":
      deletar_professor()
    elif opcao == "9":
      break
    else:
      print("Opção inválida. Tente novamente.")