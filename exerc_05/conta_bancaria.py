class ContaBancaria:
    def __init__(self, numero_conta, titular, saldo=0):
        self.__numero_conta = numero_conta
        self.__titular = titular
        self.__saldo = saldo

    # Getters
    @property
    def numero_conta(self):
        return self.__numero_conta

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    # Setters
    @numero_conta.setter
    def numero_conta(self, numero_conta):
        self.__numero_conta = numero_conta

    @titular.setter
    def titular(self, titular):
        self.__titular = titular

    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo

    # Método para depositar dinheiro na conta
    def depositar(self, valor):
        if valor > 0:
            self.__saldo = self.__saldo + valor
            print(f"Depósito de R${valor} realizado. Novo saldo: R${self.__saldo}")
        else:
            print("Valor de depósito inválido.")

    # Método para sacar dinheiro da conta
    def sacar(self, valor):
        if ((valor > 0) and (valor <= self.__saldo)):
            self.__saldo = self.__saldo - valor
            print(f"Saque de R${valor} realizado. Novo saldo: R${self.__saldo}")
        else:
            print("Valor de saque inválido ou saldo insuficiente.")

    # Método para exibir informações da conta
    def exibir_informacoes(self):
        print(f"Número da Conta: {self.__numero_conta}")
        print(f"Titular: {self.__titular}")
        print(f"Saldo: R${self.__saldo}")
