import math

class Triangulo:
    def __init__(self, base, altura):
        self.__base = base
        self.__altura = altura

    # Getters
    def get_base(self):
        return self.__base

    def get_altura(self):
        return self.__altura

    # Setters
    def set_base(self, base):
        self.__base = base

    def set_altura(self, altura):
        self.__altura = altura

    # Calcula do perimentro usando o Teorema de Pitágoras (para calcular a hipotenusa)
    def calcular_perimetro(self):
        hipotenusa = math.sqrt(self.__base**2 + self.__altura**2)
        perimetro = self.__base + self.__altura + hipotenusa

        return round(perimetro, 2)

    def calcular_area(self):
        area = (self.__base * self.__altura) / 2
        return area

# Exemplo de uso
triangulo = Triangulo(2, 6)

print("Perímetro:", triangulo.calcular_perimetro())
print("Área:", triangulo.calcular_area())
