from produto import Produto
from venda import Venda
from relatorio_de_vendas import RelatorioDeVendas

if __name__ == "__main__":
    produto1 = Produto(nome="Arroz", descricao="Arroz Tio João", preco=56, quantidade=2)
    produto2 = Produto(nome="Feijão", descricao="Feijão Broto Legal", preco=28, quantidade=1)
    venda1 = Venda(data="2024-01-15", nome_cliente="Carlos", lista_produtos=[produto1, produto2])

    produto3 = Produto(nome="Sabão em Pó", descricao="Sabão em Pó OMO", preco=36, quantidade=2)
    venda2 = Venda(data="2024-02-21", nome_cliente="Cliente 2", lista_produtos=[produto3])

    relatorio = RelatorioDeVendas(lista_vendas=[venda1, venda2])
    relatorio.gerar_relatorio_diario()

    produto4 = Produto(nome="Macarrão", descricao="Macarrão Paulista", preco=22, quantidade=1)
    venda1.atualizar_produto(produto1,produto4)

    print("\n Após atualização dos dados")
    print("===========================")
    relatorio = RelatorioDeVendas(lista_vendas=[venda1])
    relatorio.gerar_relatorio_diario()
