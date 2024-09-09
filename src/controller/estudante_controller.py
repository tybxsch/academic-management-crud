estudantes = []
def criar_estudante():
  # Lógica para criar um estudante
  nome = input("Digite o nome do estudante: ")
  estudantes.append(nome)
  print("\nEstudante criado!")

def ler_estudante():
  # Lógica para ler um estudante
  if not estudantes:
    print("\nNão há estudantes cadastrados")
  else: 
    print("\nLista de estudantes:")
    for estudante in estudantes:
      print(estudante)

def atualizar_estudante():
  # Lógica para atualizar um estudante
  print("\nEM DESENVOLVIMENTO")

def deletar_estudante():
  # Lógica para deletar um estudante
  print("\nEM DESENVOLVIMENTO")