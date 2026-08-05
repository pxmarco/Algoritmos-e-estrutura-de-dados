while True:
    try:
        expressao = input()

        pilha = []
        correta = True

        for caractere in expressao:

            if caractere == "(":
                pilha.append(caractere)  # append guarda a informação

            elif caractere == ")":
                if len (pilha) == 0:      # len realiza uma contagem 

                    correta = False
                    break

                pilha.pop()    # .pop evidencia o que foi achado e ignora o restante

        if correta and len(pilha) == 0:
            print("correct")
        else:
            print("incorrect")            

    except EOFError:  # usado quando houver uma necessidade de parar a contagem 
        break    