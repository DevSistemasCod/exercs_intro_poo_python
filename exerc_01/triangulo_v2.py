import math

class Triangulo:
    def __init__(self, base, altura):
        self.__base = base
        self.__altura = altura

    # Getters
    @property    
    def base(self):
        return self.__base

    @property    
    def altura(self):
        return self.__altura

    #Setter
    @base.setter
    def base(self, base):
        self.self.__base = base

    @altura.setter
    def altura(self, altura):
        self.__altura = altura


    def calcular_perimetro(self):
        # Calcula a hipotenusa usando o Teorema de Pitágoras
        hipotenusa = math.sqrt(self.__base**2 + self.__altura**2)
        perimetro = self.__base + self.__altura + hipotenusa

        return round(perimetro,2)


    def calcular_area(self):
        area = (self.__base * self.__altura)/2
        return area

# Exemplo de uso
triangulo = Triangulo(2,6)

print("Perímetro:", triangulo.calcular_perimetro())
print("Área:", triangulo.calcular_area())
