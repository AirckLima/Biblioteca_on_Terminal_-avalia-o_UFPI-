
caminho_relatorio = 'relatorio.txt'

def relatorio_usuario(user_dados, operacao):
    
    template_usuario = {
    'adiciona': f'o usuário {user_dados["nome"]} foi adicionado no sistema\n',
    ###
    'altera': f'o usuário {user_dados["nome"]} teve alterações ({operacao}) no sistema\n',
    ###
    'remove': f'o usuário {user_dados["nome"]} foi removido do sistema\n'
    }

    return template_usuario[operacao]

def relatorio_livro(livro_dados, operacao):

    template_livro = {
    'adiciona': f'o livro {livro_dados["nome"]} foi adicionado na biblioteca\n',
    'remove': f'o livro {livro_dados["nome"]} foi removido da biblioteca\n'
    }

    return template_livro[operacao]



def relatorio_emprestimo(emprestimo_dados, operacao):

    template_emprestimo = {
    'empresta': f'o livro {emprestimo_dados["nome"]} foi adicionado na biblioteca\n',
    'devolve': f'o livro {emprestimo_dados["nome"]} foi removido da biblioteca\n'
    }

    return template_emprestimo[operacao]



def altera_relatorio(tipo, info):

    with open(caminho_relatorio, 'a+') as relatorio:
        if tipo == 'usuario':

            texto = relatorio_usuario(info["dados"], info["operacao"])

        elif tipo == 'livro':

            texto = relatorio_livro(info["dados"], info["operacao"])

        elif tipo == 'emprestimo':

            texto = relatorio_emprestimo(info["dados"], info["operacao"])

        else:

            texto = '####### ERRO #######\n'

            
        relatorio.write(texto)

altera_relatorio("livro", {"dados":{"nome": "Pequeno_Principe"}, "operacao": 'adiciona' })