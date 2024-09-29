import time

def identificador_unico_baseado_em_timestemp():
    tempo_atual_em_microssegundos = int(time.time() * 1000000)
    identificador_5_digitos_com_base_no_tempo = tempo_atual_em_microssegundos % 100000
    return identificador_5_digitos_com_base_no_tempo
