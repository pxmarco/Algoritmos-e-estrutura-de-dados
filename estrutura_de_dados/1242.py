import sys

def par(a, b):
    return (a, b) in {("B","S"), ("S","B"), ("C","F"), ("F","C")}

def resolver(fita):
    n = len(fita)
    memo = {}

    def full(i, j):
        if i > j:
            return True
        if (j - i + 1) % 2 != 0:
            return False
        if (i, j) in memo:
            return memo[(i, j)]
        res = False
        k = i + 1
        while k <= j:
            if par(fita[i], fita[k]) and full(i + 1, k - 1) and full(k + 1, j):
                res = True
                break
            k += 2
        memo[(i, j)] = res
        return res

    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i - 1]
        for j in range(0, i):
            comprimento = i - j
            if comprimento % 2 == 0 and full(j, i - 1):
                if dp[j] + comprimento // 2 > dp[i]:
                    dp[i] = dp[j] + comprimento // 2
    return dp[n]

for linha in sys.stdin:
    fita = linha.strip()
    if not fita:
        continue
    print(resolver(fita))