# Modifique a função feita em sala velocidade() para que utilize a função divisão
 # para calcular a velocidade.

def divisao(x, y):
    return x / y

def velocidade(espaco, tempo):
    v = divisao(espaco, tempo)
    print("velocidade: {} m/s".format(v))

velocidade(100, 20)
