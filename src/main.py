# Trabalho de Eduarda Tybusch.

from view import (
    gerenciar_estudantes,
    gerenciar_professores,
    gerenciar_disciplinas,
    gerenciar_turmas,
    gerenciar_matriculas,
)
from utils.constants import INVALID_OPTION_SELECTED
from utils.colors import *


def menu_principal():
    while True:
        print("\n" + "=" * 30)
        print(f"          {WITHE}Menu Principal{RESET}          ")
        print("=" * 30)
        print(f"{GREEN}1: Gerenciar estudantes{RESET}")
        print(f"{YELLOW}2: Gerenciar professores{RESET}")
        print(f"{BLUE}3: Gerenciar disciplinas{RESET}")
        print(f"{MAGENTA}4: Gerenciar turmas{RESET}")
        print(f"{CYAN}5: Gerenciar matrículas{RESET}")
        print(f"{RED}9: Sair{RESET}")
        print("=" * 30 + "\n")

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            gerenciar_estudantes()
        elif opcao == "2":
            gerenciar_professores()
        elif opcao == "3":
            gerenciar_disciplinas()
        elif opcao == "4":
            gerenciar_turmas()
        elif opcao == "5":
            # Todo: implementar nas próximas semanas gerenciar_matriculas()
            print("EM DESENVOLVIMENTO")
        elif opcao == "9":
            print("Gerenciador finalizado.")
            break
        else:
            print(INVALID_OPTION_SELECTED)

menu_principal()
