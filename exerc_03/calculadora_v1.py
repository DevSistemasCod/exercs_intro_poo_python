import math

class Calculadora:

    def adicao(self, num1, num2):
        return num1 + num2

    def subtracao(self, num1, num2):
        return num1 - num2

    def divisao(self, num1, num2):
        if num2 != 0:
            resultado = num1 / num2
            return resultado
        else:
            mensagem = "Erro: Divisão por zero."
            return mensagem
        

    def multiplicacao(self, num1, num2):
        return num1 * num2

    def raiz_quadrada(self, num):
        if num > 0:
            raiz = math.sqrt(num)
            return raiz
        else:
            mensagem = "Erro: Raiz quadrada de número negativo."    
            return mensagem

if __name__ == "__main__":
    calculadora = Calculadora()
    print(calculadora.adicao(1,2))