lista = []


for i in range(10):
    m = int(input(f"Digite o {i+1} numero da lista: "))
    lista.append(m)

print("Lista atual: ",lista)
lista.reverse()
print("Lista reversa: ",lista)