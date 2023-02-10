def emprestarlivro():
    nome=input('qual o seu nome?')
    cadrastro=input('qual o seu cadrastro?')
    nomedolivro=input('qual o nome do livro?')
    usuario={"nome": "batista", "cadastro": 12345, "listadelivros": ["hobbit", "harry potter", "sherlock", "abc"]}
    if len(usuario['listadelivros']) > 3:
        print('voce nao pode pegar mais um livro')
    print(len(usuario['listadelivros']))



emprestarlivro()