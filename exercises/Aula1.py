import math


def print_lines():
    for i in range(1, 3):
        print()


# 1 - Imprima a frase: Python na Escola de Programação da Alura.
print("Python na Escola de Programação da Alura")
print_lines()

# 2 - Imprima a frase: Meu nome é {nome} e tenho {idade} anos em que nome e idade precisam ser valores armazenados em variáveis.
nome = "Eduardo"
idade = 34
print(f"Meu nome é {nome} e tenho {idade} anos")
print_lines()

# 3 - Imprima a palavra: ‘ALURA’ de modo que cada letra fique em uma linha, como mostrado a seguir:
for letra in "ALURA":
    print(letra)

print_lines()

# 4 - Imprima a frase: O valor arredondado de pi é: {pi_arredondado} em que o valor de pi precisa ser armazenado em uma variável e arredondado para apenas duas casas decimais. Para facilitar, utilize:
pi_value = math.pi
pi_arredondado = f"{pi_value:.2f}"
print(f"O valor arredondado de pi é: {pi_arredondado}")
