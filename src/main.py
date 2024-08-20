import alunos 
import professores
import disciplinas
import turmas
import matriculas
from utils import exibir_menu

def tratar_opcao(acao, modulo):
    if acao == 1:
        modulo.cadastrar()
    elif acao == 2:
        modulo.listar()
    elif acao == 3:
        modulo.atualizar()
    elif acao == 4:
        modulo.excluir()
    elif acao == 9:
        menu_principal()
    else:
        print("\n\nOpção incorreta!")

def menu_principal():
    print('----- MENU PRINCIPAL -----\n')
    print('(1) Gerenciar estudantes.')
    print('(2) Gerenciar professores.')
    print('(3) Gerenciar disciplinas.')
    print('(4) Gerenciar turmas.')
    print('(5) Gerenciar matrículas.')
    print('(9) Sair.\n')
    try:
        op = int(input('Informe a opção desejada: '))
    except ValueError:
        print("\n\nOpção incorreta!")
        return menu_principal()

    if op == 1:
        menu_estudantes()
    elif op == 2:
        menu_professores()
    elif op == 3:
        menu_disciplinas()
    elif op == 4:
        menu_turmas()
    elif op == 5:
        menu_matriculas()
    elif op == 9:
        print("Finalizando aplicação...")
    else:
        print("\n\nOpção incorreta!")
        menu_principal()

def menu_estudantes():
    opcoes = {1: 'Incluir', 2: 'Listar', 3: 'Atualizar', 4: 'Excluir'}
    acao = exibir_menu('ESTUDANTES', opcoes)
    if acao is not None:
        tratar_opcao(acao, alunos)

def menu_professores():
    opcoes = {1: 'Incluir', 2: 'Listar', 3: 'Atualizar', 4: 'Excluir'}
    acao = exibir_menu('PROFESSORES', opcoes)
    if acao is not None:
        tratar_opcao(acao, professores)

def menu_disciplinas():
    opcoes = {1: 'Incluir', 2: 'Listar', 3: 'Atualizar', 4: 'Excluir'}
    acao = exibir_menu('DISCIPLINAS', opcoes)
    if acao is not None:
        tratar_opcao(acao, disciplinas)

def menu_turmas():
    opcoes = {1: 'Incluir', 2: 'Listar', 3: 'Atualizar', 4: 'Excluir'}
    acao = exibir_menu('TURMAS', opcoes)
    if acao is not None:
        tratar_opcao(acao, turmas)

def menu_matriculas():
    opcoes = {1: 'Incluir', 2: 'Listar', 3: 'Atualizar', 4: 'Excluir'}
    acao = exibir_menu('MATRICULAS', opcoes)
    if acao is not None:
        tratar_opcao(acao, matriculas)

menu_principal()