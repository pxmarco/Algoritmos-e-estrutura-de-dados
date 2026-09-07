while True:
    N = int(input())

    if N == 0:
        break

    criancas = []

    for _ in range(N):
        nome, valor = input().split()
        criancas.append([nome, int(valor)])

    # A primeira criança determina o primeiro valor e a direção
    passo = criancas[0][1]

    if passo % 2 == 0:
        direcao = 1       # horário
        posicao = 1       # criança ao lado
    else:
        direcao = -1      # anti-horário
        posicao = N - 1   # criança ao lado

    while len(criancas) > 1:

        # Encontra quem será retirado
        posicao = (posicao + direcao * passo) % len(criancas)

        nome, valor = criancas.pop(posicao)

        # A ficha de quem saiu define a próxima rodada
        passo = valor

        if passo % 2 == 0:
            direcao = 1
        else:
            direcao = -1

        # Após remover, começa pelo vizinho
        if len(criancas) > 1:
            if direcao == 1:
                posicao = posicao % len(criancas)
            else:
                posicao = (posicao - 1) % len(criancas)

    print(f"Vencedor(a): {criancas[0][0]}")