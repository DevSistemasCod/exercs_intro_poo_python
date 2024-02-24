class Produto:
    def __init__(self, nome, descricao, preco, quantidade):
        self.__nome = nome
        self.__descricao = descricao
        self.__preco = preco
        self.__quantidade = quantidade

    # Getters
    @property
    def nome(self):
        return self.__nome

    @property
    def descricao(self):
        return self.__descricao

    @property
    def preco(self):
        return self.__preco

    @property
    def quantidade(self):
        return self.__quantidade

    # Setters
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @preco.setter
    def preco(self, preco):
        self.__preco = preco

    @quantidade.setter
    def quantidade(self, quantidade):
        self.__quantidade = quantidade

    def __str__(self):
        return f"Produto(nome={self.__nome}, descricao={self.__descricao}, preco={self.__preco}, quantidade={self.__quantidade})"
