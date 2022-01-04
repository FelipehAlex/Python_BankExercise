class Banco:

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    
    def extrato(self):
        print(f'Titular[{self.titular}] --> Saldo[{self.saldo:.2f}]')

    
    def depositar(self, valor):
        self.saldo += valor 

    
    def sacar(self, valor):
        self.saldo -= valor

class Itau(Banco):

    def tranferir(self, valor, destino):
        result = valor + (valor * 0.01)

        if not isinstance(destino, Bradesco):
            print('Impossivel localizar banco de destino')

        elif destino.titular == self.titular:
            print('Não é possível fazer a transação para o mesmo desconta.')

        elif result > self.saldo:
            print("Saldo insuficiente para completar a operção")

        else:
            self.sacar(result)
            destino.depositar(valor)
            print('Successful')


class Bradesco(Banco):
    
    def tranferir(self, valor, destino):
        result = valor + ((valor * 0.005) + 5)

        if not isinstance(destino, Itau):
            print('Impossivel localizar banco de destino')

        elif destino.titular == self.titular:
            print('Não é possível fazer a transação para o mesmo desconta.')

        elif result > self.saldo:
            print("Saldo insuficiente para completar a operção")

        else:
            self.sacar(result)
            destino.depositar(valor)
            print('Successful')


class Conta_teste(Banco):

    def transferir(self, valor, destino):
        self.sacar(valor + ((valor * 0.20)/100) + 10)
        destino.depositar(valor)