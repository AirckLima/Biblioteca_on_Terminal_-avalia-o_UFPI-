  
caminho = 'livros.txt'
lista_de_livros = []


def questionario():
    titulo = input("Titulo: ").lower() or 'SemTítulo'
    autor =  input("Autor(a): ").lower() or 'SemAutor'
    codigo =  input("Código: ")
    
    try:
        codigo = int(codigo)
    except:
        print('entrada de código inválida.')
    
    return [titulo, autor, codigo]



def rescrever_livros():
    
    lista_de_livros = []
    
    with open(caminho, 'w') as arquivo:
        print('.............')
    
    for n in lista_de_livros:
    
        titulo, autor, codigo = n
    
        entrada = f'titulo={titulo}.autor={autor}.codigo={codigo}\n'

        with open(caminho, 'a+') as arquivo:
            arquivo.write(entrada)



def carregar_livros():
  
    with open(caminho, 'r') as arquivo:

        arquivo_carregado = arquivo.read()

        dados = arquivo_carregado.split('\n')
        dados.pop()


    for item in dados:
        dado = item.split('.')
        livro_dados = [x for y in dado for x in y.split('=')[:-1]]
        lista_de_livros.append(livro_dados)



def confirma(operação):
    while True:
        opcao = input(f"Confirma {operação} (S/N)? ").upper()
        if opcao in "SN":
            return opcao
        else:
            print("Resposta inválida. Escolha S ou N.")



def novo_livro():
    operacao = 'cadastro_de_livro'

    titulo, autor, codigo = questionario()

    entrada = f'titulo={titulo}.autor={autor}.codigo={codigo}\n'

    resposta = confirma(operacao)

    if resposta:

        with open(caminho, 'a+') as arquivo:

            arquivo.write(entrada)



def pesquisa():

    dados_procurados = questionario()

    procurados = []

    for x in lista_de_livros:
        for y in x:
            if y in dados_procurados:
                procurados.append(x)

    if len(procurados) == 0:
        print('nada encontrado')

    print('Os livros encontrados para a sua pesquisa:')

    for n in procurados:
        print(f'{n[0]}, {n[1]}, {n[2]}')
    
    return procurados



def apaga_livro():

    operacao = 'apagar'
    lista = pesquisa()
    codigo = input('digite o codigo do livro a ser deletado: ')

    for n in lista:
        if codigo in n:

            resposta = confirma()

            if resposta == 'S':
                for x in lista_de_livros:
                    if codigo in x:
                        lista.pop(lista_de_livros.index(x))
                        break
                rescrever_livros()

    

def altera_livro():

    operacao = 'alteração'
    lista = pesquisa()
    codigo = input('digite o codigo do livro a ser alterado: ')
    novos_dados = questionario()

    for n in lista:
        if codigo in n:

            resposta = confirma()

            if resposta == 'S':
                for x in lista_de_livros:
                    if codigo in x:
                        x = novos_dados
                        break
                
                rescrever_livros()



def menu():

    print("""
   1 - Cadastrar novo livro
   2 - Alterar dados de um livro
   3 - Apagar livro
   4 - buscar
   
   0 - Sair
""")

    opcao = input('Sua opção: ')

    try:
        opcao = int(opcao)
    except:
        print('entrada inválida.')

    while True:
        
        if opcao == 0:
            break
        elif opcao == 1:
            novo_livro()
        elif opcao == 2:
            altera_livro()
        elif opcao == 3:
            apaga_livro()
        elif opcao== 4:
            pesquisa()
        else:
            print('entrada inválida')