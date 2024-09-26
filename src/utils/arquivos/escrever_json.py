import json
import os

def escrever_json(dados, nome_arquivo):
    caminho_arquivo = os.path.join('src', 'json', nome_arquivo + '.json')
    with open(caminho_arquivo, 'w') as f:
        json.dump(dados, f, indent=4)