soma=0
num=int(input("Digite quantos valores você quer calcular a média:"))
for valor in range(1,num+1):
    numero=float(input(f"Digite o {valor}° valor:"))
    soma=soma+numero
final=soma/num
print(final)