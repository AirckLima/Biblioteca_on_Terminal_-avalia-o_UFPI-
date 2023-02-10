def emprestarlivro():
    nome=input('qual o seu nome?')
    cadrastro=input('qual o seu cadrastro?')
    nomedolivro=input('qual o nome do livro?')

    listadelivros = ["hobbit", "harry potter", "sherlock", "abc"]

    usuario={"nome": nome, "cadastro": int(cadrastro), "listadelivros": listadelivros}
    
    if len(usuario['listadelivros']) > 3:
        print('voce nao pode pegar mais um livro')
    



if __name__ == "__main__":
    emprestarlivro()