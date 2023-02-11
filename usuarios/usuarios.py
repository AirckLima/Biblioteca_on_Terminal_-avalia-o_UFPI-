caminho_usuarios = 'usuarios.txt'

def adicionarUsuario (nome, email, senha, livros):
    with open(caminho_usuarios, 'a+') as usuario:

     usuario.write(f'nome: {nome}, ')
     usuario.write(f'email: {email}, ')
     usuario.write(f'Senha: {senha}, ')
     usuario.write(f'Livros: {livros}')

nome = input("Digite seu nome:\n")
email = input("Digite seu email:\n")
senha = input("Crie sua senha:\n")

adicionarUsuario(nome, email, senha, "Pequeno principe")

def alterarUsuario():
    print('Usuario alterado')

alterarUsuario()

def removerUsuario():
    print('Usuario removido')

removerUsuario()
