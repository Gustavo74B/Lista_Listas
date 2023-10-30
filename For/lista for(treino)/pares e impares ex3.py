par=0
impar=0
for num in range(0,10):
    n=int(input("Digite um número:"))
    if n%2==0:
        par=par+1
    else:
        impar=impar+1
print(f"Par = {par}")
print(f"Ímpar = {impar}")