from produto import Produto
from gerenciador_estoque import GerenciadorDeEstoque

if __name__ == "__main__":
    # Criando alguns produtos
    produto1 = Produto("Camiseta", "Camiseta de algodão", 20.0, 40.0, 50, 10)
    produto2 = Produto("Tênis", "Tênis de corrida", 80.0, 120.0, 30, 5)
    produto3 = Produto("Mochila", "Mochila para escalar", 50.0, 80.0, 15, 3)

    # Inicializando o gerenciador de estoque
    gerenciador_estoque = GerenciadorDeEstoque()

    # Adicionando produtos ao estoque
    gerenciador_estoque.adicionar_produto(produto1)
    gerenciador_estoque.adicionar_produto(produto2)
    gerenciador_estoque.adicionar_produto(produto3)

    # Consultando produtos antes da atualização de estoque
    print("Produtos antes da atualização:")
    for produto in gerenciador_estoque.consultar_produtos():
        print(produto.nome, produto.qtd_estoque)

    # Atualizando o estoque de alguns produtos
    gerenciador_estoque.atualizar_estoque("Camiseta", -5)
    gerenciador_estoque.atualizar_estoque("Tênis", 10)

    # Consultando produtos após a atualização de estoque
    print("\nProdutos após a atualização:")
    for produto in gerenciador_estoque.consultar_produtos():
        print(produto.nome, produto.qtd_estoque)
