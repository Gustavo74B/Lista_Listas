nome=input("Digite o nome do atleta:")
media=0
lista=[]
for saltos in range(1,6):
    num=float(input(f"Digite a distância do {saltos}° salto:"))
    media=media+num
    lista.append(num)
mediat=media/5
print(f"Atleta: {nome}")
print(f"Saltos: {lista}")
print(f"Média: {mediat}")