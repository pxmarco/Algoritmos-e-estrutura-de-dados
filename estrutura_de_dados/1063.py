while True:
    n = int(input())
    if n == 0:
        break

    entrada = input().split()
    destino = input().split()

    pilha = []
    operacoes = []
    posicao = 0

    for vagao in entrada:
        pilha.append(vagao)
        operacoes.append("I")

        while pilha and posicao < n and pilha[-1] == destino[posicao]:
            pilha.pop()
            operacoes.append("R")
            posicao += 1

    if posicao == n and not pilha:
        print("".join(operacoes))
    else:
        print("".join(operacoes) + " Impossible")