import math

class Calculadora:
    def __init__(self, numero1, numero2):
        self.__numero1 = numero1;
        self.__numero2 = numero2; 


    def adicao(self):
        resultado = self.__numero1 + self.__numero2
        return resultado


    def subtracao(self):
        resultado = self.__numero1 - self.__numero2
        return resultado


    def divisao(self):
        if self.__numero2 != 0:
            resultado = self.__numero1 / self.__numero2
            return resultado
        else:
            mensagem = "Erro: Divisão por zero."
            return mensagem
        

    def multiplicacao(self):
        resultado = self.__numero1 * self.__numero2
        return resultado


    def raiz_quadrada(self):
        if self.__numero > 0:
            raiz = math.sqrt(self.__numero)
            return raiz
        else:
            mensagem = "Erro: Raiz quadrada de número negativo."    
            return mensagem

if __name__ == "__main__":
    calculadora = Calculadora(2,3)
    print(calculadora.adicao())