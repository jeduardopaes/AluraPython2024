# 1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.
num = int(input("Digite um numero inteiro: "))

if num % 2 == 0:
    print(f"Numero digitado: {num} é par!")
else:
    print(f"Numero digitado: {num} é ímpar!")

print("\n\n\n")
# 2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:

# Criança: 0 a 12 anos;
# Adolescente: 13 a 18 anos;
# Adulto: acima de 18 anos.

idade = int(input("Digite sua idade: "))

if 0 <= idade <= 12:
    print(f"Você é uma criança com {idade} anos")
elif 13 <= idade <= 18:
    print(f"Você é um adolescente com {idade} anos")
else:
    print(f"Você é um adulto com {idade} anos")

print("\n\n\n")

# 3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.

usuario = input("Digite seu nome de usuário: ")
senha = input("Digite sua senha: ")

if usuario + senha == "edu1234":
    print(f"Verificado com sucesso.\nSeja Bem vindo {usuario}")
else:
    print("Credenciais inválidas.")

print("\n\n\n")

# 4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:
# Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
# Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
# Terceiro Quadrante: os valores de x e y devem ser menores que zero;
# Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
# Caso contrário: o ponto está localizado no eixo ou origem.

x = int(input("Digite um valor para X: "))
y = int(input("Digite um valor para Y: "))

if x > 0 and y > 0:
    print("O ponto está localizado no Primeiro Quadrante")
elif x < 0 and y > 0:
    print("O ponto está localizado no Segundo Quadrante")
elif x < 0 and y < 0:
    print("O ponto está localizado no Terceiro Quadrante")
elif x > 0 and y < 0:
    print("O ponto está localizado no Quarto Quadrante")
else:
    print("O ponto está localizado no eixo ou origem")
