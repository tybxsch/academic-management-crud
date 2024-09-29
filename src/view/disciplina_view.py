from utils.constants import INVALID_OPTION_SELECTED, COME_BACK_TO_MAIN_MENU
from utils.colors import *
from controller.disciplina_controller import DisciplinaController

disciplina_controller = DisciplinaController()

def gerenciar_disciplinas():
    while True:
        print("\n" + f"{BLUE}={RESET}"*30)
        print(f"{BLUE}     Gerenciando DISCIPLINAS{RESET}       ")
        print(f"{BLUE}={RESET}"*30)
        print("1: Criar disciplina")
        print("2: Listar disciplina")
        print("3: Atualizar disciplina")
        print("4: Deletar disciplina")
        print(COME_BACK_TO_MAIN_MENU)
        print("="*30 + "\n")

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            disciplina_controller.criar_disciplina()
        elif opcao == "2":
            disciplina_controller.ler_disciplina()
        elif opcao == "3":
            disciplina_controller.atualizar_disciplina()
        elif opcao == "4":
            disciplina_controller.deletar_disciplina()
        elif opcao == "9":
            break
        else:
            print(INVALID_OPTION_SELECTED)
