from collections import deque

while True:
    n = int(input())

    if n == 0:
        break
    elif n > 50:
        print("Número inválido. Digite um número até 50.\n")
        continue

    fila = deque(range(1, n + 1)) #range tem função de criar uma lista de elementos, nesse caso, de 1 até n

    descartadas = []      

    while len(fila) > 1:
        descartadas.append(str(fila.popleft()))  # popleft remove o primeiro elemento da fila e retorna ele
        fila.append(fila.popleft())  # popleft remove o primeiro elemento da fila e o retorna, append adiciona esse elemento no final da fila

    print("Discarded cards:", ", ".join(descartadas))
    print("Remaining card:", fila[0], "\n")  # fila[0] retorna o primeiro elemento da fila