quant=int(input("Digite a quantidade de números:"))
lista=[]
par=[]
impar=[]
for elementos in range(1,quant+1):
    num=int(input(f"Digite o {elementos}° número:"))
    lista.append(num)
    if num%2==0:
        par.append(num)
    elif num%2!=0:
        impar.append(num)
print(f"Números informados: {lista}")
print(f"Números pares informados: {par}")
print(f"Números ímpares informados: {impar}")