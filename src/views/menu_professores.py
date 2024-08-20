from controller import professores
from views import exibir_menu
from utils import tratar_opcao

def menu_professores():
    opcoes = {1: 'Incluir', 2: 'Listar', 3: 'Atualizar', 4: 'Excluir'}
    acao = exibir_menu('PROFESSORES', opcoes)
    if acao is not None:
        tratar_opcao(acao, professores)