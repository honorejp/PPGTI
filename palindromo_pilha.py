import string
from unicodedata import normalize


# Palíndromo é a frase ou palavra que mantém o mesmo sentido quando lida de trás pra
# frente. São exemplos de palíndromo: "arara", "osso", "reler", "somos", e “amor à roma”.
# Podemos também considerar palíndromos algumas combinações de palavras em que
# desprezamos pontuações, acentos e espaços em branco, como por exemplo: “ralo do dólar”,
# “até o poeta”, “após a sopa”, etc. Neste contexto:
# 1. Use uma Pilha para projetar uma função que recebe uma string como entrada e verifica
# se ela é ou não um palíndromo.
# 2. Use um Deque para projetar uma função que recebe uma string como entrada e verifica
# se ela é ou não um palíndromo.

# Funcao para remover acentos e espaços
def normalizarFrase(frase):
    frase = normalize('NFKD', frase).encode('ASCII', 'ignore').decode('ASCII')
    return frase.replace(' ', '')


def isPalindromo(frase):
    pilha_elementos_restantes = []
    reverso = []
    removidos = []
    tamanho = (len(frase))
    k = 1

    pilha_elementos_restantes = list(frase)

    while (k != tamanho):
        # Remove todos os elementos menos o ultimo de interesse (Desempilha o ultimo de interesse)
        for i in range(tamanho - k):
            removidos = removidos + list(pilha_elementos_restantes.pop())

        reverso = reverso + list(pilha_elementos_restantes[len(pilha_elementos_restantes) - 1])

        if (len(reverso) == int(tamanho / 2)):
            print("Lado A", reverso)

            # trata o caso das frases de tamanho impar
            if (len(frase) % 2):
                removidos.pop()

            print("Labo B", removidos)

            if (reverso == removidos):
                print("É Palindromo")
            else:
                print("Não é Palidromo")
            break

        removidos = []

        k = k + 1

        pilha_elementos_restantes = list(frase)


pass

print("Identificando Palinromos usando Filas")
entrada = input("Insira a frase: ")
print("A frase inserida foi:", entrada)
print(isPalindromo(normalizarFrase(entrada)))