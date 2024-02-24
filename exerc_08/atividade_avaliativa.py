class AtividadeAvaliativa:

    def __init__(self, lista_de_nomes, lista_de_notas):
      self.__lista_de_nomes = lista_de_nomes
      self.__lista_de_notas = lista_de_notas
    
    @property
    def lista_de_nomes(self):
        return self.__lista_de_nomes
    
    @lista_de_nomes.setter
    def lista_de_nomes(self, lista_de_nomes):
       self.__lista_de_nomes = lista_de_nomes
    
    @property
    def lista_de_notas(self):
       return self.__lista_de_notas
    
    @lista_de_notas.setter
    def lista_de_notas(self, lista_de_notas):
       self.__lista_de_notas = lista_de_notas
    

    def calcular_media_final(self):
        notas = self.__lista_de_notas
        qtd_notas = len(self.__lista_de_notas)
        lista_media_notas = []

        for i in range (qtd_notas):
            media = sum(notas[i])/len(notas[i])
            lista_media_notas.append(media)
        
        lista_de_tuplas = zip(self.__lista_de_nomes, lista_media_notas)
        dicionario_alunos_notas = dict(lista_de_tuplas)
        
        return dicionario_alunos_notas
       
