from utils.constants import INVALID_OPTION_SELECTED, COME_BACK_TO_MAIN_MENU
from utils.colors import *
from controller.matricula_controller import MatriculaController

matricula_controller = MatriculaController()

def gerenciar_matriculas():
    while True:
        print("\n" + f"{CYAN}={RESET}"*30)
        print(f"{CYAN}     Gerenciando MATRÍCULAS{RESET}       ")
        print(f"{CYAN}={RESET}"*30)
        print("1: Criar matricula")
        print("2: Listar matricula")
        print("3: Atualizar matricula")
        print("4: Deletar matricula")
        print(COME_BACK_TO_MAIN_MENU)
        print("="*30 + "\n")

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            matricula_controller.criar_matricula()
        elif opcao == "2":
            matricula_controller.ler_matricula()
        elif opcao == "3":
            matricula_controller.atualizar_matricula()
        elif opcao == "4":
            matricula_controller.deletar_matricula()
        elif opcao == "9":
            break
        else:
            print(INVALID_OPTION_SELECTED)
