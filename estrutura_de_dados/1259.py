n = int(input())
pares = []
impares = []

for _ in range(n):
    valor = int(input())
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

pares.sort()
impares.sort(reverse=True)

for v in pares:
    print(v)
for v in impares:
    print(v)