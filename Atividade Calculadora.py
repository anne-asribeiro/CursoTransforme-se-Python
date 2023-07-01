# Crie uma função calculadora() que receba dois números
# e retorne o resultado das 4 operações básicas da matemática entre eles.

def calculate():
    operation = input('''
Escolha a operação matemática que gostaria de utilizar:
+ para adição
- para subtração
* para mutiplicação
/ para divisão
''')

    numero_1 = int(input('Digite o primeiro número: '))
    numero_2 = int(input('Digite o segundo número:: '))

    if operation == '+':
        print('{} + {} = '.format( numero_1, numero_2))
        print( numero_1 + numero_2)

    elif operation == '-':
        print('{} - {} = '.format( numero_1, numero_2))
        print( numero_1 - numero_2)

    elif operation == '*':
        print('{} * {} = '.format( numero_1, numero_2))
        print( numero_1 * numero_2)

    elif operation == '/':
        print('{} / {} = '.format(numero_1, numero_2))
        print( numero_1/ numero_2)

    else:
        print('Você digitou um operador inválido, tente novamente')

    again()

def again():
    calc_again = input('''
Deseja calcular de novo?
Digite S para Sim ou N para Não.
''')

    if calc_again.upper() == 'S':
        calculate()
    elif calc_again.upper() == 'N':
        print('Fim!')
    else:
        again()

calculate()