from utils.constants import INVALID_OPTION_SELECTED, COME_BACK_TO_MAIN_MENU
from utils.colors import *
from controller import EstudanteController

estudante_controller = EstudanteController()

def gerenciar_estudantes():
    while True:
        print("\n" + f"{GREEN}={RESET}"*30)
        print(f"{GREEN}     Gerenciando ESTUDANTES{RESET}       ")
        print(f"{GREEN}={RESET}"*30)
        print("1: Criar estudante")
        print("2: Listar estudante")
        print("3: Atualizar estudante")
        print("4: Deletar estudante")
        print(COME_BACK_TO_MAIN_MENU)
        print("="*30 + "\n")

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            estudante_controller.criar_estudante()
        elif opcao == "2":
            estudante_controller.ler_estudante()
        elif opcao == "3":
            estudante_controller.atualizar_estudante()
        elif opcao == "4":
            estudante_controller.deletar_estudante()
        elif opcao == "9":
            break
        else:
            print(INVALID_OPTION_SELECTED)
