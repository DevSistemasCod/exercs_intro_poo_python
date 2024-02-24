from contato_v2 import Contato

if __name__ == "__main__":
    contato = Contato()
    contato.nome = "Carlos"
    contato.telefone = "(16)000000"
    contato.email = "testegmail.com"
    contato.exibir_conteudo()
    print(contato.__str__())
    