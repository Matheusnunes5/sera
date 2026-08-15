


n = int(input("Digite o número: "))
m = int(input("Digite o número: "))

if n > m:
    n,m=m,n

while n < m-1:
    n += 1
    print(n)