class Contato:
    # Construtor
    def __init__(self, nome = None, telefone = None, email = None):
        self.__nome = nome
        # validação do parâmetro telefone
        if(telefone != None):
            # se o atributo for válido
            if self.__validar_telefone(telefone):
                self.__telefone = telefone
            else:
                # caso contrário
                self.__telefone = ''

        # validação do parâmetro e-mail
        if(email != None):
            # se o atributo for válido
            if self.__validar_email(email):
                self.__email = email
            else:
                # caso contrário
                self.__email = ''

    #Getters
    @property
    def nome(self):
        return self.__nome
    
    @property
    def telefone(self):
        return self.__telefone 
    
    @property
    def email(self):
        return self.__email
    
    #Setters
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @telefone.setter
    def telefone(self, telefone):
        if self.__validar_telefone(telefone):
            self.__telefone = telefone
        else:
            self.__telefone = ''
            print("Telefone inválido")


    @email.setter
    def email(self, email):
        if self.__validar_email(email):
            self.__email = email
        else:
            self.__email = ''
            print("E-mail inválido")


    #Demais Métodos
            
    # Método privado utilizado para validar o e-mail        
    def __validar_email(self, email):
        if "@" not in email:
            return False
        
        if "." not in email:
            return False
        
        # endswith método de string para verificar/validar se 
        # a string termina com uma determina substring
        if not email.endswith("com"):
            return False
        
        return True
    
    # Método privado utilizado para validar o telefone
    def __validar_telefone(self, telefone):
        apenas_digitos_tel = ''

        for caracter in str(telefone):
            if caracter.isdigit():
                apenas_digitos_tel = apenas_digitos_tel + caracter
        
        #validação qtd de digitos
        if(len(apenas_digitos_tel) == 10) or (len(apenas_digitos_tel) == 11):
            return True
        else:
            return False
        
    # será aexibido apenas conteúdos diferentes de None (vazio)
    def exibir_conteudo(self):
        if(self.__nome != None):
            print(f"Nome: {self.__nome}")

        if(self.__telefone != None):
            print(f"Telefone: {self.__telefone}")
       
        if(self.__email != None):
            print(f"Email: {self.__email}")

    # método usado para retornar uma string com os atributos do objeto
    def __str__(self):
        return f"Nome: {self.__nome},Telefone: {self.__telefone}, Email: {self.__email}"

        
    