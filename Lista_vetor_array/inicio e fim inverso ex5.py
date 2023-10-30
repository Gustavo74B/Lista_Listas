comeco=int(input("Digite o começo:"))
fim=int(input("Digite o fim:"))
lista=[]
for element in range(fim,comeco-1,-1):
    lista.append(element)
print(lista)