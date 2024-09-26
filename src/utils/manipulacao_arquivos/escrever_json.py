import json

def escrever_json(dados, nome_arquivo):
    with open(nome_arquivo + '.json', 'w') as f:
        json.dump(dados, f, indent=4)
        f.close()