# Ana Beatriz Papa, Giovanna Moreira, Guilherme Miranda, Juliana Mendes, Leticia Cardoso e Maria Manuela Ribeiro

# Função para ler os dados do arquivo de registro
def ler_registro():
    dados = []
    with open("registro.txt", "r") as arquivo:
        for linha in arquivo:
            dados.append(tuple(linha.strip().split(',')))
    return dados

# Função para solicitar ao usuário a parte de um nome e imprimir na tela os nomes de clientes existentes no arquivo
def buscar_por_parte_nome(dados):
    parte_nome = input("Digite a parte de um nome: ").lower()
    clientes_encontrados = set()
    for cliente, _, _, _ in dados:
        if parte_nome in cliente.lower():
            clientes_encontrados.add(cliente)
    if clientes_encontrados:
        print("Clientes encontrados:")
        for cliente in clientes_encontrados:
            print(cliente)
    else:
        print("Nenhum cliente encontrado com essa parte do nome.")

# Função para solicitar ao usuário o nome completo de um cliente e imprimir na tela o(s) número(s) do(s) caso(s) associado(s) a ele
def buscar_numero_casos(dados):
    nome_cliente = input("Digite o nome completo do cliente: ").lower()
    numeros_casos = []
    for cliente, numero, _, _ in dados:
        if nome_cliente == cliente.lower():
            numeros_casos.append(numero)
    if numeros_casos:
        print("Número(s) do(s) caso(s) associado(s) ao cliente:")
        for numero in numeros_casos:
            print(numero)
    else:
        print("Nenhum caso encontrado para esse cliente.")

# Função para solicitar ao usuário um número de caso e imprimir na tela o nome do cliente, a despesa, a receita e a diferença entre receita e despesa do caso
def detalhes_caso(dados):
    numero_caso = input("Digite o número do caso: ")
    encontrado = False
    for cliente, numero, despesa, receita in dados:
        if numero_caso == numero:
            print("Nome do cliente:", cliente)
            print("Despesa:", despesa)
            print("Receita:", receita)
            print("Diferença entre receita e despesa:", float(receita) - float(despesa))
            encontrado = True
            break
    if not encontrado:
        print("Nenhum caso encontrado com esse número.")

# Função para imprimir na tela a despesa total
def calcular_despesa_total(nome_arquivo):
    despesa_total = 0
    with open('registro.txt', 'r') as arquivo:
        next(arquivo)  # Pular a primeira linha
        for linha in arquivo:
            _, _, despesa, _ = linha.strip().split(',')
            despesa_total += float(despesa)
    print(despesa_total)

# Nome do arquivo de registro
nome_arquivo = "registro.txt"  # Substitua pelo nome do seu arquivo

# Testando a função
print("Despesa total:", calcular_despesa_total('registro.txt'))

# Função para imprimir na tela a receita total
def calcular_receita_total(nome_arquivo):
    receita_total = 0
    with open('registro.txt', 'r') as arquivo:
        next(arquivo)  # Pular a primeira linha
        for linha in arquivo:
            _, _, _, receita = linha.strip().split(',')
            receita_total += float(receita)
    print(receita_total)

# Nome do arquivo de registro
nome_arquivo = "registro.txt"  # Substitua pelo nome do seu arquivo


print("Receita total:", calcular_receita_total('registro.txt'))

# Função para imprimir na tela o nome do cliente, número, receita e despesa do caso com a maior despesa
def imprimir_maior_despesa(dados):
    dados_sem_cabecalho = dados[1:]
    maior_despesa = max(dados_sem_cabecalho, key=lambda x: float(x[2]))
    print("Maior despesa:")
    print("Nome do cliente:", maior_despesa[0])
    print("Número do caso:", maior_despesa[1])
    print("Receita:", maior_despesa[3])
    print("Despesa:", maior_despesa[2])
    

# Função para imprimir na tela o nome do cliente, número, receita e despesa do caso com a maior receita
def imprimir_maior_receita(dados):
    dados_sem_cabecalho = dados[1:]
    maior_receita = max(dados_sem_cabecalho, key=lambda x: float(x[3]))
    print("Maior receita:")
    print("Nome do cliente:", maior_receita[0])
    print("Número do caso:", maior_receita[1])
    print("Receita:", maior_receita[3])
    print("Despesa:", maior_receita[2])

# Função para solicitar ao usuário o nome completo de um cliente e gravar um arquivo contendo os números, as receitas e despesas de cada caso associado a ele, além de conter o total de despesas, receitas e a diferença entre esses totais
def gravar_detalhes_cliente(dados):
    nome_cliente = input("Digite o nome completo do cliente: ").lower()
    casos_cliente = [(numero, float(despesa), float(receita)) for cliente, numero, despesa, receita in dados if nome_cliente == cliente.lower()]
    if not casos_cliente:
        print("Nenhum caso encontrado para esse cliente.")
        return
    total_despesas = sum(despesa for _, despesa, _ in casos_cliente)
    total_receitas = sum(receita for _, _, receita in casos_cliente)
    diferenca = total_receitas - total_despesas
    with open(nome_cliente + "_detalhes.txt", "w") as arquivo:
        arquivo.write("Detalhes do cliente: " + nome_cliente + "\n")
        arquivo.write("Número\tDespesa\tReceita\n")
        for caso in casos_cliente:
            arquivo.write("\t".join(map(str, caso)) + "\n")
        arquivo.write("Total de despesas: " + str(total_despesas) + "\n")
        arquivo.write("Total de receitas: " + str(total_receitas) + "\n")
        arquivo.write("Diferença entre receitas e despesas: " + str(diferenca) + "\n")

# Função para exibir o menu
def exibir_menu(dados):
    while True:
        print("\nMenu:")
        print("a) Buscar por parte do nome do cliente")
        print("b) Buscar número do caso associado a um cliente")
        print("c) Detalhes de um caso específico")
        print("d) Imprimir na tela a despesa total")
        print("e) Imprimir na tela a receita total")
        print("f) Imprimir na tela o caso com a maior despesa")
        print("g) Imprimir na tela o caso com a maior receita")
        print("h) Gravar detalhes de um cliente em arquivo")
        print("x) Sair")

        opcao = input("Escolha uma opção: ").lower()

        if opcao == 'a':
            buscar_por_parte_nome(dados)
        elif opcao == 'b':
            buscar_numero_casos(dados)
        elif opcao == 'c':
            detalhes_caso(dados)
        elif opcao == 'd':
            calcular_despesa_total(dados)
        elif opcao == 'e':
            calcular_receita_total(dados)
        elif opcao == 'f':
            imprimir_maior_despesa(dados)
        elif opcao == 'g':
            imprimir_maior_receita(dados)
        elif opcao == 'h':
            gravar_detalhes_cliente(dados)
        elif opcao == 'x':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

# Função principal
def main():
    # Ler os dados do arquivo de registro
    dados = ler_registro()
    # Exibir o menu
    exibir_menu(dados)

# Chamando a função principal
if __name__ == "__main__":
    main()
