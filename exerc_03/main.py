from exerc_02.calculadora_v1 import Calculadora

class Main:
    def __init__(self):
        self.calculadora = Calculadora()

  

if __name__ == "__main__":
    main = Main()
    print(main.calculadora.adicao(1,2))