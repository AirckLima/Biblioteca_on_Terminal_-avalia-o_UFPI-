caminho_usuarios = 'usuarios.txt'

def adicionarUsuario (nome, email, senha,):
    with open(caminho_usuarios, 'a+') as usuario:
     usuario.write(f'nome: {nome}\n')
     usuario.write(f'email: {email}\n')
     usuario.write(f'Senha: {senha}\n')

nome = input("Digite seu nome:\n")
email = input("Digite seu email:\n")
senha = input("Crie sua senha:\n")

adicionarUsuario(nome, email, senha)

def alterarUsuario():
    print('Usuario alterado')

def removerUsuario():
    print('Usuario removido')
