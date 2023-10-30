quant=int(input("Digite a quantidade de notas:"))
lista=[]
submedia=0
for elementos in range(1,quant+1):
    nota=float(input(f"Digite a {elementos}° nota:"))
    submedia=submedia+nota
media=submedia/quant
print("Sua média é:",media)