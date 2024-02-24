class GerenciadorDeEstoque:
    def __init__(self):
        self.produtos_cadastrados = []

    def adicionar_produto(self, produto):
        self.produtos_cadastrados.append(produto)

    def remover_produto(self, nome):
        for produto in self.produtos_cadastrados:
            if produto.nome == nome:
                self.produtos_cadastrados.remove(produto)
                return True
        return False

    def atualizar_estoque(self, nome, quantidade):
        for produto in self.produtos_cadastrados:
            if produto.nome == nome:
                produto.qtd_estoque += quantidade
                return True
        return False

    def consultar_produtos(self):
        return self.produtos_cadastrados
