caminho = 'emprestimo.txt' 

def emprestarlivro():

    nome=input('qual o seu nome?')
    
    cadrastro=input('qual o seu cadrastro?')
    
    nomedolivro=input('qual o nome do livro?')
    
    tipo = input('qual vai ser seu tipo de emprestimo? ')
    
    listadelivros = ["hobbit", "harry potter", "sherlock", "abc"]

        
    # if len(usuario['listadelivros']) > 3:
    #     print('voce nao pode pegar mais um livro')


    # linha modelo para guardar nos arquivos
    linha = f'tipo={tipo}.cadastro={cadrastro}.dia={"hoje"}.livro={nomedolivro}\n'
    

    with open(caminho, 'a+') as arquivo:
        arquivo.write(linha)




if __name__ == "__main__":
    print(emprestarlivro())

# v - recebe os dados do emprestimo
# c - verifica quantos livros a pessoa tem
# v - escreve os emprestimos no aquivo
# f - ler o arquivo e verificar os dados
# f - modificar os dados








