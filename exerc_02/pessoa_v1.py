class Pessoa:
    def __init__(self, nome = None, altura = None, peso = None):
        self.__nome = nome
        self.__altura = altura
        self.__peso = peso

    # Getters
    def get_nome(self):
        return self.__nome
    
    def get_altura(self):
        return self.__altura
    
    def get_peso(self):
        return self.__peso
    
    # Setters
    def set_nome(self, nome):
        self.__nome = nome

    def set_altura(self, altura):
        if(altura > 0):
            self.__altura = altura
        else:
            print("Altura inválida !!!")
    
    
    def set_peso(self, peso):
        if(peso > 0):
            self.__peso = peso
        else:
            print("Peso inválida !!!")

#################################################
### Calcular ICMC ###
    def calcular_imc(self):
        altura_quadrado = (self.__altura ** 2)
        imc = (self.__peso / altura_quadrado)
    
        if imc < 16:
            mensagem = "Magreza grave"
            return mensagem
        
        elif (16 <= imc) and (imc <= 16.9):
            mensagem = "Magreza moderada"
            return mensagem
        
        elif (17 <= imc) and (imc <= 18.5):
            mensagem = "Magreza leve"
            return mensagem
        
        elif (18.6 <= imc) and (imc <= 24.9):
            mensagem = "Peso ideal"
            return mensagem
    
        elif (25 <= imc) and (imc <= 29.9):
            mensagem = "Sobrepeso"
            return mensagem
        
        elif (30 <= imc) and (imc <= 34.9):
            mensagem = "Obesidade grau I"
            return mensagem
        
        elif (35 <= imc) and (imc <= 39.9):
            mensagem = "Obesidade grau II ou severa"
            return mensagem
        
        else:
            mensagem = "Obesidade grau III ou mórbida"
            return mensagem
        

### Imprimir Dados da Informações ###
    def imprimir_dados(self):
        print(f"Nome: {self.__nome}")
        print(f"Altura: {self.__altura}")
        print(f"Peso: {self.__peso}")
        
if __name__ == "__main__":
    pessoa = Pessoa();
    
    pessoa.set_nome("Carlos")
    pessoa.set_altura(1.50)
    pessoa.set_peso(50)
    pessoa.imprimir_dados()
    print(pessoa.calcular_imc())