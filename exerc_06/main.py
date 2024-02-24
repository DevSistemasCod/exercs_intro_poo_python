from livro import Livro

if __name__ == "__main__":
    # Exemplo de uso
    livro1 = Livro("Dom Casmurro", "Machado de Assis", "Romance", 300)
    livro2 = Livro("Memórias Póstumas de Brás Cubas", "Machado de Assis", "Romance", 250)
    livro3 = Livro("Pense em Python", "Allen B. Downey", "Programação", 200)

    lista_livros = [livro1, livro2, livro3]

    # Exibir informações dos livros cadastrados
    for livro in lista_livros:
        livro.exibir_informacoes()

    # Listar livros do tema "romance"
    tema_pesquisado = input("Digite o tema para listar os livros: ")
    livros_do_tema = Livro.listar_livros_por_tema(lista_livros, tema_pesquisado)

  
    # Exibir informações dos livros do tema pesquisado
    if len(livros_do_tema) > 0:
        print(f"===== Livros com o Tema: {tema_pesquisado}")
        for livro in livros_do_tema:
            livro.exibir_informacoes()