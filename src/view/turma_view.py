from controller import criar_turma, ler_turma, atualizar_turma, deletar_turma
from utils.constants import INVALID_OPTION_SELECTED, COME_BACK_TO_MAIN_MENU
from utils.colors import *

def gerenciar_turmas():
  while True:
    print("\n" + f"{MAGENTA}={RESET}"*30)
    print(f"{MAGENTA}     Gerenciando TURMAS{RESET}       ")
    print(f"{MAGENTA}={RESET}"*30)
    print("1: Criar turma")
    print("2: Listar turma")
    print("3: Atualizar turma")
    print("4: Deletar turma")
    print(COME_BACK_TO_MAIN_MENU)
    print("="*30 + "\n")

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
      print(INVALID_OPTION_SELECTED)