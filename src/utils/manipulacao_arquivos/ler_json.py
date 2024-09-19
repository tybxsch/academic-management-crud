import json

def ler_json(caminho_arquivo):
  dados = {}
  try:
    with open(caminho_arquivo + '.json', 'r') as f:
      dados = json.load(f)
      f.close()
      return dados
  except FileNotFoundError:
    print('Arquivo não encontrado')
    return dados