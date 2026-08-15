soma = 0
for i in range(5):
    soma += int(input(f"Digite o {i+1} numero: "))

media = soma / 5
print(f"A soma dos numeros inseridos é: {soma}")
print(f"A media dos numeros inseridos é: {media:.2f}")