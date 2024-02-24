from conta_bancaria import ContaBancaria



if __name__ == "__main__":
    # Exemplo de uso
    conta = ContaBancaria(numero_conta="12345", titular="Carlos", saldo=1000)
    conta.exibir_informacoes()

    conta.depositar(500.0)
    conta.sacar(200.0)
