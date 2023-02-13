livro = []
# Variável para marcar uma alteração na agenda
alterada = False

def pede_titulo():
    return input("Titulo: ")


def pede_autor():
    return input("Autor(a): ")


def mostra_dados(titulo, autor):
    print(f"Titulo: {titulo}; Autor(a): {autor}")


def pede_nome_arquivo():
    return input("Nome do arquivo: ")


def pesquisa(titulo):
    mtitulo = titulo.lower()
    for p, e in enumerate(livro):
        if e[0].lower() == mtitulo:
            return p
    return None


def novo():
    global livro, alterada
    titulo = pede_titulo()
    autor = pede_autor()
    livro.append([titulo, autor])
    alterada = True
    

def confirma(operação):
    while True:
        opção = input(f"Confirma {operação} (S/N)? ").upper()
        if opção in "SN":
            return opção
        else:
            print("Resposta inválida. Escolha S ou N.")


def apaga():
    global agenda
    titulo = pede_titulo()
    p = pesquisa(titulo)
    if p is not None:
        if confirma("apagamento") == "S":
            del livro[p]
            alterada = True
    else:
        print("Título não encontrado.")
    
    
def altera():
    p = pesquisa(pede_titulo())
    if p is not None:
        titulo = livro[p][0]
        autor = livro[p][1]
        print("Encontrado:")
        mostra_dados(titulo, autor)
        titulo = pede_titulo()
        autor = pede_autor()
        if confirma("alteração") == "S":
            livro[p] = [titulo, autor]
            alterada = True
    else:
        print("Título não encontrado.")


def lista():
    print("\nlivro\n\n------")
    # Usamos a função enumerate para obter a posição do livro
    for posição, e in enumerate(livro):
        # Imprimimos a posição, sem saltar linha
        print(f"Posição: {posição}", end="")
        mostra_dados(e[0], e[1])
    print("------\n")


def lê_última_lista_gravada():
    última = última_lista()
    if última is not None:
        leia_arquivo(última)


def última_lista():
    try:
        arquivo = open("ultima lista.dat", "r", encoding="utf-8")
        última = arquivo.readline()[:-1]
        arquivo.close()
    except FileNotFoundError:
        return None
    return última


def atualiza_última(nome):
    arquivo = open("ultima lista.dat", "w", encoding="utf-8")
    arquivo.write(f"{nome}\n")
    arquivo.close()


def grava():
    global alterada
    if not alterada:
        print("Você não alterou a lista. Deseja gravá-la mesmo assim?")
        if confirma("gravação") == "N":
            return
    print("Gravar\n------")
    nome_arquivo = pede_nome_arquivo()
    arquivo = open(nome_arquivo, "w", encoding="utf-8")
    for e in livro:
        arquivo.write(f"{e[0]}#{e[1]}\n")
    arquivo.close()
    alterada = False


def valida_faixa_inteiro(pergunta, inicio, fim):
    while True:
        try:
            valor = int(input(pergunta))
            if inicio <= valor <= fim:
                return valor
        except ValueError:
            print(f"Valor inválido, favor digitar entre {inicio} e {fim}")


def menu():
    print("""
   1 - Novo
   2 - Altera
   3 - Apaga
   4 - Lista
   5 - Grava
   
   0 - Sai
""")
    print(f"\ntitulos de livro: {len(livro)}\n")
    return valida_faixa_inteiro("Escolha uma opção: ", 0, 6)


while True:
    opção = menu()
    if opção == 0:
        break
    elif opção == 1:
        novo()
    elif opção == 2:
        altera()
    elif opção == 3:
        apaga()
    elif opção == 4:
        lista()
    elif opção == 5:
        grava()