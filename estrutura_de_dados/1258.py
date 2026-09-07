mapa_tamanho = {'P': 0, 'M': 1, 'G': 2}
primeiro_caso = True

while True:
    n = int(input())
    if n == 0:
        break

    if not primeiro_caso:
        print()
    primeiro_caso = False

    camisetas = []
    for _ in range(n):
        nome = input()
        cor, tamanho = input().split()
        camisetas.append((cor, tamanho, nome))

    camisetas.sort(key=lambda c: (c[0], mapa_tamanho[c[1]], c[2]))

    for cor, tamanho, nome in camisetas:
        print(cor, tamanho, nome)