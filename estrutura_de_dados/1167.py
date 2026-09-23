while True:
    N = int(input())
    if N == 0:
        break

    criancas = []

    for _ in range(N):
        nome, valor = input().split()
        criancas.append([nome, int(valor)])

    posicao = 0
    while len(criancas) > 1:
        valor = criancas[posicao][1]
        if valor % 2 == 0:
            posicao = (posicao + valor) % len(criancas)
        else:
            posicao = (posicao - valor) % len(criancas)
        criancas.pop(posicao)
    print(f"Vencedor(a): {criancas[0][0]}")