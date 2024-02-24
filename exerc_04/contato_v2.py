class Contato:
    # Sem construtor 

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
        
    # exibir o conteúdo dos atributos
    def exibir_conteudo(self):
        print(f"Nome: {self.__nome}")
        print(f"Telefone: {self.__telefone}")
        print(f"Email: {self.__email}")

    # método usado para retornar uma string com os atributos do objeto
    def __str__(self):
        return f"Nome: {self.__nome},Telefone: {self.__telefone}, Email: {self.__email}"

        
    