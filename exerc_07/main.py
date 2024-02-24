from filme import Filme


from filme import Filme

if __name__ == "__main__":
    filme1 = Filme("Filme 1", Filme.ADOLESCENTE_I, 120)
    filme2 = Filme("Filme 2", Filme.JOVEM, 90, 2022)
    filme3 = Filme("Filme 3", Filme.CRIANCA, 100, 2021)
    filme4 = Filme("Filme 4", Filme.ADOLESCENTE_I, 75)

    # Definindo ano de lançamento depois de instância do objeto
    filme1.set_ano_lancamento(2023)
    filme4.set_ano_lancamento(2024)

    # Alterando a duração de um filme
    filme1.alterar_duracao(70)

    # Imprimindo informações de um filme
    print("\nDetalhes do Filme 1:")
    print(f"Título: {filme1.get_titulo()}")
    print(f"Classificação: {filme1.get_classificacao()}")
    print(f"Duração: {filme1.get_duracao()} minutos")
    print(f"Ano de Lançamento: {filme1.get_ano_lancamento()}\n")

    # Verificando a classificação etária para um espectador de 15 anos
    idade_espectador = 15
    

    # Listando filmes disponíveis para um espectador de 14 anos
    print(f"Filmes disponíveis para um espectador de {idade_espectador} anos: {Filme.filmes_disponiveis(idade_espectador)}\n")
