frase="Teria sido melhor assistir o filme de Pele"
print(frase.count("a", 2, 10))
    

print("mariana".index("a"))
print("mariana".index("a", 2))
print("mariana".index("a",5, 7))
print("Mariana".index("ana"))
#print("Mariana".index("x"))

def bombom(dinheiro,preco):
    return float(dinheiro)//preco, dinheiro%preco

def maisbombom(dinheiro,preco):
    return preco - bombom(dinheiro,preco)[1]

def lista(n):
    if n%2==0:
        return list(range(2,n+1,2))
    else:
        return list(range(2,n,2))
    