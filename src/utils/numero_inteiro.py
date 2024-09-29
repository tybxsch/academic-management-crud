from utils.constants import INSERT_INT_NUMBER
def obter_codigo_inteiro(mensagem):
    while True:
        try:
            codigo = int(input(mensagem))
            return codigo
        except ValueError:
            print(INSERT_INT_NUMBER)
