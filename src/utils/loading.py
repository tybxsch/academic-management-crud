import time, sys

# Função de fake loading
def loading(loading_message = "Carregando..."):
    print(loading_message)
    for i in range(0, 100):
        time.sleep(0.03)
        sys.stdout.write(u"\u001b[1000D" + str(i + 1) + "%")
        sys.stdout.flush()
    print