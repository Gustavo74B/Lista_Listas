quant=int(input("Digite a quantidade de números:"))
lista=[]
indice=-1
for element in range(quant):
    indice=indice+1
    num=int(input(f"Digite o número com índice {indice}:"))
    lista.append(num*2)
print(lista)