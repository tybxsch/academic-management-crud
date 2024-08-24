from controller import criar_estudante, ler_estudante, atualizar_estudante, deletar_estudante
from utils.constants import INVALID_OPTION_SELECTED, COME_BACK_TO_MAIN_MENU
from utils.colors import *

def gerenciar_estudantes():
  while True:
    print("\n" + f"{GREEN}={RESET}"*30)
    print(f"{GREEN}     Gerenciando ESTUDANTES{RESET}       ")
    print(f"{GREEN}={RESET}"*30)
    print("1: Criar estudante")
    print("2: Ler estudante")
    print("3: Atualizar estudante")
    print("4: Deletar estudante")
    print(COME_BACK_TO_MAIN_MENU)
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
      print(INVALID_OPTION_SELECTED)