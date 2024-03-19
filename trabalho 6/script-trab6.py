# Variáveis
numeros = [15, 35, 40, 60]
frase = "Olá, meu nome é Giovanna"
palavra = "Coração"

# Calculando a média aritmética dos números
media = sum(numeros) / len(numeros)
print("Média aritmética dos números:", media)

# Calculando o quadrado de um dos números (segundo número)
numero_quadrado = numeros[1] ** 2
print("Quadrado do segundo número:", numero_quadrado)

# Calculando o dobro de um dos números (terceiro número)
numero_dobro = numeros[2] * 2
print("Dobro do terceiro número:", numero_dobro)

# Calculando a quantidade de letras na palavra
quantidade_letras = len(palavra)
print("Quantidade de letras na palavra:", quantidade_letras)

# Calculando a quantidade de espaços em branco na frase
quantidade_espacos = frase.count(" ")
print("Quantidade de espaços em branco na frase:", quantidade_espacos)

# Verificando se o primeiro número é maior que o segundo
primeiro_maior = numeros[0] > numeros[1]
print("O primeiro número é maior que o segundo:", primeiro_maior)

# Encontrando o maior número
maior_numero = max(numeros)
print("O maior número é:", maior_numero)

