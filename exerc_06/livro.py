class Livro:
    def __init__(self, titulo, autor, tema, num_paginas):
        self.__titulo = titulo
        self.__autor = autor
        self.__tema = tema
        self.__num_paginas = num_paginas

    #Getters
    @property
    def titulo(self):
        return self.__titulo

    @property
    def autor(self):
        return self.__autor
    
    @property
    def tema(self):
        return self.__tema

    @property
    def num_paginas(self):
        return self.num__paginas

    # Setters
    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @autor.setter
    def autor(self, autor):
        self.__autor = autor

    @tema.setter
    def tema(self, tema):
        self.__tema = tema

    @num_paginas.setter
    def num_paginas(self, num_paginas):
        self.__num_paginas = num_paginas

    # Exibir Informações 1
    def exibir_informacoes(self):
        print(f"Título: {self.__titulo}")
        print(f"Autor: {self.__autor}")
        print(f"Tema: {self.__tema}")
        print(f"Número de Páginas: {self.__num_paginas}")
        print("\n")
    
    # Exibir Informações 2
    def __str__(self):
        return f"Livro: {self.__titulo}, {self.__autor}, {self.__tema}, {self.__num_paginas}"

    @staticmethod
    def listar_livros_por_tema(livros, tema):
        livros_do_tema = []
        
        for livro in livros:
            if livro.tema.lower() == tema.lower():
                livros_do_tema.append(livro)
                
        return livros_do_tema







