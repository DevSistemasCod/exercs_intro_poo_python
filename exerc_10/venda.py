class Venda:
    def __init__(self, data, nome_cliente, lista_produtos):
        self.__data = data
        self.__nome_cliente = nome_cliente
        self.__lista_produtos = lista_produtos

    # Getters
    @property
    def data(self):
        return self.__data

    @property
    def nome_cliente(self):
        return self.__nome_cliente

    @property
    def lista_produtos(self):
        return self.__lista_produtos

    # Setters
    @data.setter
    def data(self, data):
        self.__data = data

    @nome_cliente.setter
    def nome_cliente(self, nome_cliente):
        self.__nome_cliente = nome_cliente

    @lista_produtos.setter
    def lista_produtos(self, lista_produtos):
        self.__lista_produtos = lista_produtos

    # Método para adicionar em uma lista
    def adicionar_produto(self, produto):
        self.__lista_produtos.append(produto)

    # Método para remover da lista de produtos
    def remover_produto(self, produto):
        if produto in self.__lista_produtos:
            self.__lista_produtos.remove(produto)

    # Método para atualizar item da lista de produtos
    def atualizar_produto(self, produto_antigo, produto_novo):
        if produto_antigo in self.__lista_produtos:
            indice = self.__lista_produtos.index(produto_antigo)
            self.__lista_produtos[indice] = produto_novo

    # criação do método __str__
    def __str__(self):
        return f"Venda(data={self.__data}, nome_cliente={self.__nome_cliente}, lista_produtos={self.__lista_produtos})"