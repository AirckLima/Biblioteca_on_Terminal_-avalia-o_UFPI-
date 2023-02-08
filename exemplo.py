numero = 10.5  #declarei uma VARIÁVEL

OUTRO_NUMERO = 199 #declarei uma CONSTANTE

soma = numero + 3.0  #podemos usar o valor de uma variável só mencionando o nome dela

print(soma)

# entrada = input()  # sempre retorna uma STRING

# TIPOS DE DADOS
#  string -> 'oi tudo bem'     " isso também é uma string "
#      obs.: o tipo de dado string é IMUTÁVEL
#            as strings são uma sequência de caracteres onde cada um tem um INDICE
# 
#  numero (inteiro, float) -> 14  -56   64.53   0


texto = 'oi'

#        01234567      ---- indices
texto = 'iae, vamos lá'.strip(',') # usando o . pode-se chamar um MÉTODO

print(texto[3])    #aqui, podemos acessar apenas um caratere

print(texto[3:7])  #aqui, podemos acessar uma "fatia" da sting original


qualquer_coisa = '20'

print('quero escrever um numero' + qualquer_coisa + 'adfs')

print(f'o numero é: {qualquer_coisa}')

variavel = [1,3,4,'12',[1,3,4]] 

abc = "string"

print(print(2))

livro = {'nome': 'pequeno principe'}

print(livro['nome'])

dado, carta, moeda = 20, 'yu-gi-oh', True