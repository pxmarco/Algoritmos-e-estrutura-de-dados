while True:
    try:
        n = int(input())
    except EOFError:
        break

    numeros = [input() for _ in range(n)]
    total = 0

    for i in range(1, n):
        anterior = numeros[i - 1]
        atual = numeros[i]
        limite = min(len(anterior), len(atual))

        iguais = 0
        for j in range(limite):
            if anterior[j] == atual[j]:
                iguais += 1
            else:
                break  # assim que diferir, para de contar

        total += iguais

    print(total)