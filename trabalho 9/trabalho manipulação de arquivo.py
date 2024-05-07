def salvar_nome_em_arquivo():
    nome = input("Por favor, informe seu nome: ")
    # Abre o arquivo no modo de escrita (modo 'w')
    with open('nome.txt', 'w') as arquivo:
        # Escreve o nome no arquivo
        arquivo.write(nome)
    print("Seu nome foi salvo no arquivo 'nome.txt'.")

# Chamada da função
salvar_nome_em_arquivo()

def imprimir_conteudo_arquivo():
    # Solicita ao usuário o nome do arquivo
    nome_arquivo = input("Por favor, informe o nome do arquivo de texto: ")
    # Abre o arquivo no modo de leitura (modo 'r')
    with open(nome_arquivo, 'r') as arquivo:
        # Lê o conteúdo do arquivo
        conteudo = arquivo.read()
        # Imprime o conteúdo do arquivo
        print("Conteúdo do arquivo:")
        print(conteudo)

# Chamada da função
imprimir_conteudo_arquivo()

def copiar_conteudo_para_novo_arquivo():
    # Nome do arquivo de exemplo
    nome_arquivo_original = "nome.txt"
    # Nome do novo arquivo
    nome_novo_arquivo = "nome_nova_versao.txt"

    # Abre o arquivo de exemplo no modo de leitura (modo 'r')
    with open(nome_arquivo_original, 'r') as arquivo_original:
        # Lê o conteúdo do arquivo de exemplo
        conteudo = arquivo_original.read()
        
        # Abre o novo arquivo no modo de escrita (modo 'w')
        with open(nome_novo_arquivo, 'w') as novo_arquivo:
            # Escreve o conteúdo lido no novo arquivo
            novo_arquivo.write(conteudo)
    
    print(f"O conteúdo do arquivo '{nome_arquivo_original}' foi copiado para o arquivo '{nome_novo_arquivo}'.")

# Chamada da função
copiar_conteudo_para_novo_arquivo()

def encontrar_nome_por_numero():
    # Solicita ao usuário um número
    numero = input("Informe um número: ")

    # Nome do arquivo de exemplo
    nome_arquivo = "arquivo-exemplo.txt"

    # Abre o arquivo no modo de leitura (modo 'r')
    with open(nome_arquivo, 'r') as arquivo:
        # Percorre cada linha do arquivo
        for linha in arquivo:
            # Divide a linha em número e nome, considerando a vírgula como separador
            partes = linha.split(';')
            numero_arquivo = partes[0].strip()  # remove espaços em branco
            nome = partes[1].strip()  # remove espaços em branco

            # Se o número na linha for igual ao número fornecido pelo usuário, imprime o nome correspondente
            if numero_arquivo == numero:
                print(f"O nome correspondente ao número {numero} é: {nome}")
                return  # Termina a função após encontrar o nome correspondente

    # Se o número não for encontrado no arquivo
    print(f"Não foi encontrado um nome correspondente ao número {numero}.")

# Chamada da função
encontrar_nome_por_numero()

