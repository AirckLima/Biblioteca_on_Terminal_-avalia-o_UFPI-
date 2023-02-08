caminho_arquivo = 'livros.txt'

with open(caminho_arquivo, 'w+') as arquivo:
    print(type(arquivo))
    arquivo.write('hello world\n')
    arquivo.seek(0,0)
    print(arquivo.read())

    arquivo.write('hello world!!!!!\n')
    arquivo.seek(0,0)
    print(arquivo.read())

