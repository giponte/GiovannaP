f = open('meu_arquivo.txt', 'w')

f.write("Teste de número 1\n") # '\n' gera uma quebra de linha

f.write("teste de número 2\n")

f.close()

f = open('meu_arquivo.txt', 'a')

f.write('Mais um pouco de texto')

f.close()

# abre um novo arquivo, escreve e fecha
f = open('novo_arquivo.txt', 'w')
f.write('Novos arquivos\nnovos textos')
f.close()
f = open('novo_arquivo.txt', 'r+')
conteudo = f.read() # conteudo = 'Novos arquivos\nnovos textos'
f.seek(0) # é preciso voltar ao início para ler outra vez
print(f.read())

f.write('\nNunca é demais')
f.close()
f = open('novo_arquivo.txt', 'r')
print(f.read())

f = open("novo_arquivo.txt", "r")
for linha in f:
    print(linha)
    
f.seek(0)

for linha in f:
    print(linha, end='')