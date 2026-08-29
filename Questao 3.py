m = input("Digite o nome do aluno: ")
soma = 0
notas = []

for i in range (4):
    n = float(input(f"Digite a {i+1}° nota: "))
    notas.append(n)
    soma = soma+n
    media = soma/4

print("\n Boletim de", m)
print("-----------------------")

for i in notas:
    print(i)

print("-----------------------")
print(f"A soma das notas de {m} é {soma:.1f}")
print(f"A media das notas de {m} é {media:.1f}")