while True:
    X, Y, P = map(int, input().split())

    if X == 0 and Y == 0 and P == 0:
        break

    Q = int(input())

    campo = [[0] * Y for _ in range(X)]

    saida = []

    for _ in range(Q):
        partes = input().split()

        if partes[0] == "A":
            N, Xc, Yc = int(partes[1]), int(partes[2]), int(partes[3])
            campo[Xc][Yc] += N
        else:
            X1, Y1, X2, Y2 = int(partes[1]), int(partes[2]), int(partes[3]), int(partes[4])

            if X1 > X2:
                X1, X2 = X2, X1
            if Y1 > Y2:
                Y1, Y2 = Y2, Y1

            total = 0
            for x in range(X1, X2 + 1):
                for y in range(Y1, Y2 + 1):
                    total += campo[x][y]

            saida.append(str(total * P))

    print("\n".join(saida))
    print()