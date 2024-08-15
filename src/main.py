from alunos import cadastrar_aluno, listar_alunos, atualizar_aluno, excluir_aluno

def menu():
  while True:
    print("----- MENU -----")
    print("1. Cadastrar aluno")
    print("2. Listar alunos")
    print("3. Atualizar aluno")
    print("4. Excluir aluno")
    print("0. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
      cadastrar_aluno()
    elif opcao == "2":
      listar_alunos()
    elif opcao == "3":
      atualizar_aluno()
    elif opcao == "4":
      excluir_aluno()
    elif opcao == "0":
      break
    else:
      print("Opção inválida. Tente novamente.")

menu()