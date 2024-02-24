class RelatorioDeVendas:
    def __init__(self, lista_vendas):
        self.lista_vendas = lista_vendas

    def gerar_relatorio_diario(self):
        print("Relatório Diário de Vendas:")
        
        for venda in self.lista_vendas:
            print(f"Data: {venda.data}")
            print(f"Cliente: {venda.nome_cliente}")
            print("Produtos:")

            for produto in venda.lista_produtos:
                print(f" Nome: {produto.nome}")
                print(f" Descrição: {produto.descricao}")
                print(f" Preço: R${produto.preco}")
                print(f" Quantidade: {produto.quantidade}")
                print("  ------------------------------")