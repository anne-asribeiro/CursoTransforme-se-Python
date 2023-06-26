import random

def calcular_pontuacao(chute, numero_secreto):
    return abs(chute - numero_secreto)

def jogar_adivinhacao():
    print(" Jogo da adivinhação!")
    print("Selecione o grau de dificuldade:")
    print("1 - Fácil (8 tentativas)")
    print("2 - Médio (5 tentativas)")
    print("3 - Difícil (2 tentativas)")

    nivel = int(input("Informe o grau de dificuldade: "))
    if nivel == 1:
        num_tentativas = 8
    elif nivel == 2:
        num_tentativas = 5
    elif nivel == 3:
        num_tentativas = 2
    else:
        print("Nível inválido. O jogo será encerrado.")
        return

    numero_secreto = random.randint(0, 100)
    pontos = 500

    for tentativa in range(1, num_tentativas + 1):
        print(f"Tentativa {tentativa} de {num_tentativas}")
        chute = int(input("Digite um número entre 0 e 100: "))

        if chute < 0 or chute > 100:
            print("Chute inválido. Tente novamente.")
            continue

        diferenca = calcular_pontuacao(chute, numero_secreto)
        pontos -= diferenca

        if chute == numero_secreto:
            print("Parabéns! Você acertou!")
            print(f"Pontuação final: {pontos} pontos")
            break
        elif tentativa == num_tentativas:
            print("Suas tentativas acabaram!")
            print(f"O número secreto era: {numero_secreto}")
            print("Fim de jogo.")
        else:
            if chute < numero_secreto:
                print("Chute um número maior!")
            else:
                print("Chute um número menor!")
            print(f"Pontuação atual: {pontos} pontos")

jogar_adivinhacao()
