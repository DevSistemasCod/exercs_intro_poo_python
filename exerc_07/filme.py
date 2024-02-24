class Filme:
    # Constantes de classificação
    CRIANCA = 10
    ADOLESCENTE_I = 12
    ADOLESCENTE_II = 14
    JOVEM = 16
    ADULTO = 18

    # Todas as instâncias de classe usarão a mesma lista
    __filmes_criados = []

    def __init__(self, titulo, classificacao, duracao, ano_lancamento=None):
        self.__titulo = titulo
        self.__classificacao = classificacao
        self.__duracao = duracao
        self.__ano_lancamento = ano_lancamento

        # Adiciona o filme à lista quando criado
        self.__adicionar_filme_lista()

    # Getters
    def get_titulo(self):
        return self.__titulo

    def get_classificacao(self):
        return self.__classificacao

    def get_duracao(self):
        return self.__duracao
    
    def get_ano_lancamento(self):
        return self.__ano_lancamento

    # Setters
    def set_ano_lancamento(self, ano_lancamento):
        self.__ano_lancamento = ano_lancamento

    def alterar_duracao(self, nova_duracao):
        if nova_duracao >= 0:
            self.__duracao = nova_duracao
            print(f"Duração do filme '{self.__titulo}' alterada para {self.__duracao} minutos.")
        else:
            print("A duração do filme não pode ser um valor negativo.")

  
    def __classificacao_etaria(self, idade_espectador):
        return idade_espectador >= self.__classificacao


    @staticmethod
    def filmes_disponiveis(idade_espectador):
        filmes_pode_assistir = []

        for filme in Filme.__filmes_criados:
            if filme.__classificacao_etaria(idade_espectador):
                filmes_pode_assistir.append(filme.get_titulo())

        return filmes_pode_assistir



    # Método privado para adicionar filme à lista
    def __adicionar_filme_lista(self):
        Filme.__filmes_criados.append(self)



