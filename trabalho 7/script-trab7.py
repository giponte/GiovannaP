def calcular_soma_e_media(lista):
    soma = sum(lista)
    media = soma / len(lista)
    return soma, media

def substituir_palavra(lista, palavra_procurada, nova_palavra):
    for i in range(len(lista)):
        if lista[i] == palavra_procurada:
            lista[i] = nova_palavra
    return lista

def gerar_triangulo(numero_linhas):
    for i in range(1, numero_linhas + 1):
        print('*' * i)

# Exemplos de uso:

# Soma e média de lista de números
lista_numeros = [1, 2, 3, 4]
soma, media = calcular_soma_e_media(lista_numeros)
print("Soma:", soma)
print("Média:", media)

# Substituir as ocorrências de uma palavra por outra em uma lista de palavras
lista_palavras = ["banana", "morango", "limão"]
palavra_procurada = "banana"
nova_palavra = "maçã"
nova_lista = substituir_palavra(lista_palavras, palavra_procurada, nova_palavra)
print("Lista alterada:", nova_lista)

# Triângulo de asteriscos
numero_linhas = 4
gerar_triangulo(numero_linhas)

