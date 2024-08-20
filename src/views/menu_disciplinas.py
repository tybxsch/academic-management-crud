from controller import disciplinas
from views import exibir_menu
from utils import tratar_opcao

def menu_disciplinas():
    opcoes = {1: 'Incluir', 2: 'Listar', 3: 'Atualizar', 4: 'Excluir'}
    acao = exibir_menu('DISCIPLINAS', opcoes)
    if acao is not None:
        tratar_opcao(acao, disciplinas)