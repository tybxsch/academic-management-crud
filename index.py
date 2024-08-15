def cadastrar_aluno():
  # Lógica para cadastrar um novo aluno
  pass

def listar_alunos():
  # Lógica para listar todos os alunos cadastrados
  pass

def atualizar_aluno():
  # Lógica para atualizar os dados de um aluno
  pass

def excluir_aluno():
  # Lógica para excluir um aluno
  pass

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