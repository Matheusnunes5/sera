lista = []

#roda 5 vezes pro ususario digitar os 5 numeros
for i in range(5):
    num = int(input(f"digite o {i+1} numero"))
    lista.append(num)

print("os numeros inseridos na lista sao: ")
#exibe cada item da lista
for i in lista:
    print(i)
