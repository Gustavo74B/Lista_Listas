quant=int(input("Digite a quantidade de números:"))
lista=[]
soma=0
mult=1
for elementos in range(1,quant+1):
    num=int(input(f"Digite o {elementos}° número:"))
    soma=soma+num
    mult=mult*num
    lista.append(num)
print(f"Números informados: {lista}")
print(f"Soma: {soma}")
print(f"Multiplicação: {mult}")