from controller import criar_professor, ler_professor, atualizar_professor, deletar_professor
from utils.constants import INVALID_OPTION_SELECTED, COME_BACK_TO_MAIN_MENU
from utils.colors import *

def gerenciar_professores():
  while True:
    print("\n" + f"{YELLOW}={RESET}"*30)
    print(f"{YELLOW}     Gerenciando PROFESSORES{RESET}       ")
    print(f"{YELLOW}={RESET}"*30)
    print("1: Criar professor")
    print("2: Ler professor")
    print("3: Atualizar professor")
    print("4: Deletar professor")
    print(COME_BACK_TO_MAIN_MENU)
    print("="*30 + "\n")

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
      print(INVALID_OPTION_SELECTED)