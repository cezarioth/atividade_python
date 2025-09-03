class ContaBancaria:

    def __init__(self, saldo_inicial: float):

        self._saldo = saldo_inicial

    @property

    def saldo(self):

        return self._saldo

    def depositar(self, valor: float):

        if valor > 0:

            self._saldo += valor
    
        else:

            print("Valor de depósito inválido!")

    def sacar(self, valor: float):

        if 0 < valor <= self._saldo:

            self._saldo -= valor

        else:

            print("Saldo insuficiente ou valor inválido!")

