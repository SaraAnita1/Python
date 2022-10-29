#Aprendendo Hello World 
#Aula 1

from cgi import print_environ
from turtle import end_fill


print ("Gostosa, porem cansada!")
print ("Hello World")
print ("¬¬")
print ("que seja sucesso")

#Aprendendo Váriaveis e constantes em python
    #Aula 2

age = 25
name = 'Sara'
print(f'Meu nome é {name} e eu tenho {age} ano(s) de idade')

age, name = (25, 'Sara')
print(f'meu nome é {name} e eu tenho {age} anos de idade')

age = 24
name = 'Vitor'
igual = 'Amor da minha vida'
print (f'O nome dele é {name} ele tem {age} de idade, conhecido tambem como {igual}.')

age = 25
name = 'Sara'
igual = 'Amor da vida do Vitor'
print (f'O meu nome é {name} eu tenho {age} de idade, conhecida tambem como {igual}.')

    #constantes
    #ela nasce e permanece com o mesmo valor.

#não existe palavra para determinar que é uma constante = para fazer isso você deve utilizar o nome da váriavel todo em maiusculo.
#assim como combinado por convenção.
        #Boas Práticas
# 1 - Padrão de nomes deve ser em snake case
    #todos os espaços vazios deve ser colocados _
# 2 - Escolher nomes Sugestivos.
    #exemplo: sempre dizer de fato o que a variavel está fazendo naquele código.
# 3 - Nome de Constante sempre em maiúsculo.


name = 'Sara'
age = 25

name, age = 'Vitor', 24

print (name, age)

limite_saque_diario = 1000

BRAZILIAN_STATES = ["SP", "RJ", "SC", "RS"]
print (BRAZILIAN_STATES)


#Conversão de tipos
#aula 3

    #inteiro > float

preco = 10
print(preco)
#>>>10 

preco = float(preco)
print(preco)
#>>>10.0

preco = 10/2
print(preco)
#>>>5.0

    #Float para Inteiro

preco = 10.30
print(preco)
#>>> 10.3

preco = int(preco)
print(preco)
#>>> 10

    #conversão por divisão

preco = 10
print(preco)
#>>>10

print(preco/2)
#>>>5.0

print(preco//2)
#>>>5

    #numero para string

preco = 10,50
idade = 28

print(str(preco))
#>>>10.5

print(str(idade))
#>>> 28

texto = f"idade {idade} preco {preco}"
print(texto)
#>>>idade 28 preco 10.5

    #String para Numero

preco = "10.50"
idade = "28"

print(float(preco))
#>>>10.50

print(int(idade))
#>>>28

    #Possiveis erros de conversão

#preco = "python"
#print(float(preco))

#>>> ValueError: could not convert string to float: 'python'

print(int(1.9756435))
print(int("10"))
print(float("10.10"))
print(float(100.0))

print(type(str(10.10)))
valor = 10
valor_str = str(valor)
print(type(valor))
print(type(valor_str))

print(100/2)
print(100//2)

#segunda / só significa que você quer que o programa retorne o numero inteiro

    #funções de entrada e de saida
    #aula 4

#lendo valores com a função input

#função usada para quando querermos ler dados de entrada padrão(teclado). Ela recebe um argumento do tipo string, que é exibido para o usuario na saida padrão(tela). A função lê a entrada, converte para string e retorna o valor.

#nome = input("Informe o seu nome:")
#>>> informe o seu nome 

#exibindo valores com a função print

nome = "Guilherme"
sobrenome = "Carvalho"

print(nome, sobrenome)
print(nome, sobrenome, end="...\n")
print(nome,sobrenome, sep="#")
        #\n = quebra de linha

nome = input("Informe o seu nome:")
idade = input ("Informe sua Idade:")

print(nome,idade)
print(nome, idade, end="...\n")
print(nome,idade, sep="#")

