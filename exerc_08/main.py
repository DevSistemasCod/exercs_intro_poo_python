from atividade_avaliativa import AtividadeAvaliativa

if __name__ == "__main__":
    
    qtd_alunos = int(input("Informe a quantidade de alunos: "))
    qtd_provas = int(input("Informe a quantidade de provas: "))
    lista_nomes = []
    lista_notas = []
    lista_de_lista_notas = []

    for i in range(qtd_alunos):
        nome = input(f"Informe o nome do aluno {i}: ")
        lista_nomes.append(nome)

        lista_notas = []
        for j in range(qtd_provas):
            nota = float(input("Informe a nota: "))
            lista_notas.append(nota)
        lista_de_lista_notas.append(lista_notas)
        

    atividade_avaliativa = AtividadeAvaliativa(lista_nomes, lista_de_lista_notas)
    print(atividade_avaliativa.calcular_media_final())
