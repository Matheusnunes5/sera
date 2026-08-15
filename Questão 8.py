a = float(input("Digite o número: "))
b = float(input("Digite o número: "))
c = float(input("Digite o número: "))
d = float(input("Digite o número: "))
e = float(input("Digite o número: "))

soma = a+b+c+d+e

print(f"a soma do numeros digitados é {soma}")

média = a+b+c+d+e / 5

print(f"a média dos numeros digitados é {média}")



#for i in range(5):
#    n = float(input("Digite o numero"))
#soma += n
#media = soma / 5
#print(f"A media é {media}")


soma = 0
for i in range(5):
    soma += int(input("Digite um numero: "))

media = soma / 5
print(f"A soma dos numeros inseridos é {soma} e a media é {media}")