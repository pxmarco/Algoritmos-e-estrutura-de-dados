try:
    while True:
        expressao = input()

        pilha = []
        contagem = 0

        for caractere in expressao:
            if caractere == "<":
                pilha.append(caractere)
            elif caractere == ">":
                if len(pilha) > 0:
                    pilha.pop()
                    contagem += 1

        print(contagem)

except EOFError:
    pass