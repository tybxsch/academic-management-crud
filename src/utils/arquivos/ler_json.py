import json
import os

def ler_json(nome_arquivo):
    caminho_arquivo = os.path.join('src', 'json', nome_arquivo + '.json')
    if os.path.exists(caminho_arquivo):
        with open(caminho_arquivo, 'r') as f:
            dados = json.load(f)
            if isinstance(dados, list):
                return dados
            else:
                return []
    return []