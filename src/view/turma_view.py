from utils.constants import INVALID_OPTION_SELECTED, COME_BACK_TO_MAIN_MENU
from utils.colors import *
from controller.turma_controller import TurmaController

turma_controller = TurmaController()

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
            turma_controller.criar_turma()
        elif opcao == "2":
            turma_controller.ler_turma()
        elif opcao == "3":
            turma_controller.atualizar_turma()
        elif opcao == "4":
            turma_controller.deletar_turma()
        elif opcao == "9":
            break
        else:
            print(INVALID_OPTION_SELECTED)
