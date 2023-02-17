  
caminho = 'usuarios.txt'
lista_de_usuario = []


def questionario():
    nome = input("Nome: ").lower() or 'SemNome'
    cadastro =  input("Cadastro: ").lower() 

    
    try:
        cadastro = int(cadastro)
    except:
        print('entrada de cadastro inválida.')
    
    return [nome, cadastro]



def rescrever_usuario():
    
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
        usuario_dados = [x for y in dado for x in y.split('=')[:-1]]
        lista_de_usuario.append(usuario_dados)



def confirma(operação):
    while True:
        opcao = input(f"Confirma {operação} (S/N)? ").upper()
        if opcao in "SN":
            return opcao
        else:
            print("Resposta inválida. Escolha S ou N.")



def novo_usuario():
    operacao = 'cadastro_de_livro'

    nome, cadastro, livros = questionario()

    entrada = f'nome={nome}.cadastro={cadastro}.livros={livros}\n'

    resposta = confirma(operacao)

    if resposta:

        with open(caminho, 'a+') as arquivo:

            arquivo.write(entrada)



def pesquisa():

    dados_procurados = questionario()

    procurados = []

    for x in lista_de_usuario:
        for y in x:
            if y in dados_procurados:
                procurados.append(x)

    if len(procurados) == 0:
        print('nada encontrado')

    print('Os usuarios encontrados para a sua pesquisa:')

    for n in procurados:
        print(f'{n[0]}, {n[1]}, {n[2]}')
    
    return procurados



def apaga_usuario():

    operacao = 'apagar'
    lista = pesquisa()
    codigo = input('digite o codigo do livro a ser deletado: ')

    for n in lista:
        if codigo in n:

            resposta = confirma()

            if resposta == 'S':
                for x in lista_de_usuario:
                    if codigo in x:
                        lista.pop(lista_de_usuario.index(x))
                        break
                rescrever_usuario()

    

def altera_livro():

    operacao = 'alteração'
    lista = pesquisa()
    codigo = input('digite o codigo do livro a ser alterado: ')
    novos_dados = questionario()

    for n in lista:
        if codigo in n:

            resposta = confirma()

            if resposta == 'S':
                for x in lista_de_usuario:
                    if codigo in x:
                        x = novos_dados
                        break
                
                rescrever_usuario()



def menu():

    print("""
   1 - Cadastrar novo usuario
   2 - Alterar dados de um usuario
   3 - Apagar usuario
   
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
            novo_usuario()
        elif opcao == 2:
            altera_livro()
        elif opcao == 3:
            apaga_usuario()
        else:
            print('entrada inválida')