def imprimir_info(nome, idade, cidade, sep='\n', end='\n'):
    print(f"Nome: {nome}", end=sep)
    print(f"Idade: {idade}", end=sep)
    print(f"Cidade: {cidade}", end=end)

# Exemplo de uso da função
imprimir_info("Eduardo", 30, "Maricá", sep=' | ', end='\n\n')
imprimir_info("Mônica", 35, "Rio de Janeiro", sep=' | ', end='\n\n')


def calcular():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    # Solicita a operação desejada
    operacao = input("Digite a operação desejada (+, -, *, /): ")
    
    # Verifica se a operação é de adição
    if operacao == '+':
        resultado = num1 + num2
        print(f"O resultado da adição é: {resultado}")
    else:
        print("Operação inválida!")

# Exemplo de uso da função
calcular()

def criar_lista_compras():
    # Solicita ao usuário os itens da lista de compras
    entrada = input("Digite os itens da lista de compras, separados por vírgula: ")

    # Divide a entrada do usuário em uma lista de itens
    itens = entrada.split(',')

    # Imprime os itens em linhas separadas usando um loop
    print("Lista de compras:")
    for item in itens:
        print(item.strip())  # strip() remove espaços em branco extras ao redor do item

# Exemplo de uso da função
criar_lista_compras()


def converter_para_fahrenheit():
    # Solicita ao usuário a temperatura em graus Celsius
    celsius = float(input("Digite a temperatura em graus Celsius: "))

    # Converte a temperatura para Fahrenheit usando a fórmula
    fahrenheit = (celsius * 9/5) + 32

    # Imprime o resultado da conversão
    print(f"A temperatura em Fahrenheit é: {fahrenheit} °F")

# Exemplo de uso da função
converter_para_fahrenheit()

def pedir_nomes():
    nomes = []

    while True:
        nome = input("Digite um nome (ou 'sair' para encerrar): ")
        if nome.lower() == 'sair':
            break
        nomes.append(nome)

    print("Nomes digitados:")
    for nome in nomes:
        print(nome)

# Exemplo de uso da função
pedir_nomes()
