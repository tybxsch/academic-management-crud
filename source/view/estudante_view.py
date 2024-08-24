from controller import criar_estudante, ler_estudante, atualizar_estudante, deletar_estudante

def gerenciar_estudantes():
  while True:
    print("\n" + "="*30)
    print("Gerenciando estudantes")
    print("="*30)
    print("1: Criar estudante")
    print("2: Ler estudante")
    print("3: Atualizar estudante")
    print("4: Deletar estudante")
    print("9: Voltar para o menu principal")
    print("="*30 + "\n")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
      criar_estudante()
    elif opcao == "2":
      ler_estudante()
    elif opcao == "3":
      atualizar_estudante()
    elif opcao == "4":
      deletar_estudante()
    elif opcao == "9":
      break
    else:
      print("Opção inválida. Tente novamente.")