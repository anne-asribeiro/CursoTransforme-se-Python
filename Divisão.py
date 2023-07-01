# Crie uma função divisão(), que receba dois números como parâmetros
# e retorne o resultado da divisão do primeiro pelo segundo.

nummero_1 = float(input("Digite um número: "))
numero_2 = float(input("Digite outro número: "))

divisao = nummero_1 / numero_2
resto = nummero_1 % numero_2
print()
print(nummero_1, "divido por", numero_2, "é igual a: ", divisao)
print("O resto da divisão entre", nummero_1, "e", numero_2, " é igual a:", resto)