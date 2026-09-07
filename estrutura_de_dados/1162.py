total_casos = int(input())

for _ in range(total_casos):
    tamanho = int(input())
    vagoes = list(map(int, input().split())) if tamanho > 0 else []

    trocas = 0
    for i in range(tamanho):
        for j in range(0, tamanho - 1 - i):
            if vagoes[j] > vagoes[j + 1]:
                vagoes[j], vagoes[j + 1] = vagoes[j + 1], vagoes[j]
                trocas += 1

    print(f"Optimal train swapping takes {trocas} swaps.")