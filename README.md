1) Crie uma classe chamada Triangulo capaz de representar um triângulo. Essa classe deve ter os seguintes atributos (base e altura):
A classe deve ter os seguintes métodos:
Método para calcular perimetro: 
A fórmula do perímetro:   P = lado1 + lado2 + lado3

Se não temos um lado podemos calculá-lo da seguinte forma:
considere que temos b = base e a = altura e queremos o c (hipotenusa)
c = sqrt(base**2 + altura**2)
ou seja a hipotenusa é calculada por meio do cálculo da raiz da soma dos catetos ao quadrado.

Método para calcular área:
area = (base * altura)/2.

Faça também Métodos getters e setters.

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

2) Implemente uma classe para representar uma pessoa, como os atributos nome, idade, peso e altura. Crie os métodos públicos necessários para sets e gets, também faça um método para imprimir os dados de uma pessoa. Por fim faça um método capaz de calcular o IMC da pessoa e informar em qual situação ela se encontra 
Obs1: IMC (Índice de Massa Corpórea) de uma pessoa.
Para fazer o cálculo do IMC devemos efetuar os seguintes passos. 
1) Multiplique o valor de sua altura (em metros) por ele mesmo. 
Ex: se você medir 1,60 metros, o cálculo será: 1,6 x 1,6 = 2,56
2) Dividir o peso pelo valor obtido acima. 
Se o seu peso for 60 quilos, a conta será: 60 ÷ 2,56 = 23,43

Classifique o resultado obtido:
menores que 16 — magreza grave; 
entre 16 e 16,9 — magreza moderada; 
entre 17 e 18,5 — magreza leve; 
entre 18,6 e 24,9 — peso ideal; 
entre 25 e 29,9 — sobrepeso; 
entre 30 e 34,9 — obesidade grau I; 
entre 35 e 39,9 — obesidade grau II ou severa; 
maiores do que 40 — obesidade grau III ou mórbida.

Obs2:   Crie uma instância para a sua  classe e faça os testes de funcionalidade necessários para validar o seu funcionamento.

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

3) Escreva um código em Python utilizando OO para as seguintes operações, sua classe deve chamar Calculadora.
- Cálculo da Adição 
- Cálculo da Subtração 
- Cálculo da Divisão (trate o caso Zero) 
- Cálculo da Multiplicação 
- Cálculo da Raiz Quadrada
- Sair

Obs: siga o paradigma de Orientação a Objetos.
Crie uma instância para a sua  classe e faça os testes de funcionalidade necessários para validar o seu funcionamento.

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

4) Implemente em Python uma classe chamada Contato, ela deve ter os seguintes atributos:
nome: nome do contato.
telefone: número de telefone do contato.
email: endereço de e-mail do contato.

 A classe deve ter um método para exibir o conteúdo da classe ou o __str__ que retorna uma representação em string.
 Além disso, implemente:
- Um método chamado validar_email que verifica se o formato do e-mail é válido (contém "@", "." e “com”).
- Um método para validar telefone (contém 2 digitos para código e 8-9 digitos para o número)
 Tais métodos são métodos que devem ser usados como métodos auxiliares para os setters de email e telefone.

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

5)  Em programação Python faça uma classe chamada ContaBancaria, ela deve ter os seguintes atributos:
 numero_conta: número da conta bancária.
 titular: nome do titular da conta.
 saldo: saldo disponível na conta.

 Além disso, a classe deve ter os seguintes métodos:
método __init__: Construtor que inicializa os atributos da conta.
método depositar(valor): Adiciona um valor ao saldo da conta.
método sacar(valor): Retira um valor do saldo da conta, desde que haja saldo suficiente.
método para exibir o conteúdo do objeto

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

6) Implemente uma classe Python chamada Livro que será utilizada para representar informações sobre livros em uma biblioteca. A classe deve conter os seguintes elementos:
Atributos:
titulo: Título do livro.
autor: Autor do livro.
tema: Tema do livro.
num_paginas: Número de páginas do livro.

Métodos:
Getters: titulo(), autor(), tema(), num_paginas()
Setters: titulo(titulo), autor(autor), tema(tema),num_paginas(num_paginas)
exibir_informacoes(): Método que exibe informações detalhadas sobre o livro, incluindo título, autor, tema e número de páginas.

Método Estático:
listar_livros_por_tema(livros, tema): Método estático que recebe uma lista de livros e um tema como parâmetros e retorna uma lista de livros que têm o tema especificado.

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

7)  Desenvolva um código em Python para gerenciar filmes e classificações etárias, para isso implemente uma classe chamada Filme que permitirá a criação de objetos filmes, cada um com seu título, classificação etária, duração e ano de lançamento.
A classe Filme deve ter as seguintes funcionalidades:
Atributos:
titulo: Título do filme.
classificacao: Classificação etária do filme (constantes disponíveis: CRIANCA, ADOLESCENTE_I, ADOLESCENTE_II, JOVEM, ADULTO).
duracao: Duração do filme em minutos.
ano_lancamento: Ano de lançamento do filme (opcional).

Métodos:
get_titulo():  get_classificacao():  get_duracao():  get_ano_lancamento(): 
set_ano_lancamento(ano_lancamento): 

alterar_duracao(nova_duracao): Altera a duração do filme para o valor especificado.
__classificacao_etaria(idade_espectador): Método privado que verifica se um espectador com a idade especificada pode assistir ao filme com base na classificação etária.
filmes_disponiveis(idade_espectador): Método estático que retorna uma lista de títulos de filmes disponíveis para um espectador com a idade especificada.

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

8)  Faça uma implementação em Python para gerenciar as notas dos alunos. Uma das principais funcionalidades deste código é calcular a média final de cada aluno.
  Para calcular a média final é necessário considerar as notas obtidas pelo aluno em cada atividade avaliativa e a quantidade de atividades feitas. Para isso considere implementar um método chamado média que recebe uma lista de notas.
 Podemos criar uma classe chamada "AtividadeAvaliativa" essa classe pode ter os seguintes atributos:
 lista_de_nomes: nomes dos alunos
 lista_de_notas: lista de notas do aluno
 implemente os metodos gets e sets para os atributos da classe
 método para calcular a média final de cada aluno (tal método pode retornar um dicionário de dados com a relação entre nome e média)

 Crie uma instância para a sua  classe e faça os testes de funcionalidade necessários para validar o seu funcionamento.

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

9) Faça um código Python para gerenciar um sistema de estoque, cada produto deve ser cadastrado com as seguintes informações: nome, descrição, preço de compra, preço de venda, quantidade em estoque e quantidade mínima em estoque. Assim, você pode  criar uma classe "Produto" que contém os atributos nome, descrição, preço de compra, preço de venda, quantidade em estoque e quantidade mínima em estoque. 

Além disso, é possível criar uma classe "GerenciadorDeEstoque" que contém uma lista de produtos cadastrados e métodos para adicionar, remover, atualizar e consultar produtos. 
 Por exemplo, o método de adicionar um novo produto pode receber como parâmetro um objeto da classe Produto e adicionar esse objeto na lista de produtos cadastrados. O método de atualizar a quantidade em estoque de um produto pode receber como parâmetro o nome do produto e a quantidade a ser adicionada ou removida do estoque, e então atualizar o objeto correspondente na lista de produtos.
 O método de consultar produtos pode retornar a lista de produtos cadastrados para ser exibida na tela para o usuário.

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

10) Faça um código Python para gerar um relatório de vendas, cada venda registrada deve conter as seguintes informações: data da compra, nome do cliente, lista de produtos comprados (cada produto contém nome, descrição, preço e quantidade comprada).

Para resolver esse problema com código orientado a objetos, você pode criar uma classe "Venda" que contém as seguintes informações: data da compra, nome do cliente e lista de produtos. 
A lista de produtos pode ser representada como uma lista de objetos da classe "Produto", que possui os atributos nome, descrição, preço e quantidade. 
Além disso, é possível criar uma classe "RelatorioDeVendas" que recebe uma lista de vendas e gera o relatório diário de vendas. 

