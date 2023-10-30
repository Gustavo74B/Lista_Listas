tab=int(input("Digite o número que você quer fazer a tabuada:"))
comeco=int(input("Digite o começo da tabuada:"))
fim=int(input("Digite o fim da tabuada:"))
if fim<comeco:
    print("Valor inválido")
elif comeco<fim:
    for contador in range(comeco,fim+1):
        print(f"{tab} X {contador} = {tab*contador}")
else:
    print(f"{tab} X {comeco} = {tab*comeco}")