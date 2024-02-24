class Produto:
    def __init__(self, nome, descricao, preco_compra, preco_venda, qtd_estoque, qtd_minima_estoque):
        self.__nome = nome
        self.__descricao = descricao
        self.__preco_compra = preco_compra
        self.__preco_venda = preco_venda
        self.__qtd_estoque = qtd_estoque
        self.__qtd_minima_estoque = qtd_minima_estoque

    #Getters
    @property
    def nome(self):
        return self.__nome
    
    @property
    def descricao(self):
        return self.__descricao
    
    @property
    def preco_compra(self):
        return self.__preco_compra
    
    @property
    def preco_venda(self):
        return self.__preco_venda
    
    @property
    def qtd_estoque(self):
        return self.__qtd_estoque
    
    @property
    def qtd_minima_estoque(self):
        return self.__qtd_minima_estoque
    
    #Setters
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao
    
    @preco_compra.setter
    def preco_compra(self, preco_compra):
        self.__preco_compra = preco_compra
    
    @preco_venda.setter
    def preco_venda(self, preco_venda):
        self.__preco_venda = preco_venda
    
    @qtd_estoque.setter
    def qtd_estoque(self, qtd_estoque):
        self.__qtd_estoque = qtd_estoque
    
    @qtd_minima_estoque.setter
    def qtd_minima_estoque(self, qtd_minima_estoque):
        self.__qtd_minima_estoque = qtd_minima_estoque

    def exibir_conteudo(self):
        print(f"Nome: {self.__nome}")
        print(f"Descrição: {self.__descricao}")
        print(f"Preço de Compra: {self.__preco_compra}")
        print(f"Preço de Venda: {self.__preco_venda}")
        print(f"Quantidade em Estoque: {self.__qtd_estoque}")
        print(f"Quantidade Mínima em Estoque: {self.__qtd_minima_estoque}")