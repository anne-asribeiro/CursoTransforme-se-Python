class Conta:
    contador = 0

    def __init__(self, cliente):
        Conta.contador += 1
        self.titular = cliente
        self.numero = Conta.contador
        self.saldo = 0
        self.identificador = f"CONTA-{self.numero}"

    def depositar(self, valor):
        self.saldo += valor

    def transferir(self, destino, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            destino.saldo += valor
        else:
            print("Saldo insuficiente para transferência.")

    def extrato(self):
        print("Extrato da Conta:")
        print("Titular:", self.titular.nome)
        print("Número:", self.numero)
        print("Saldo:", self.saldo)
        print("Identificador:", self.identificador)
