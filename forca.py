
def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo de Forca!***")
    print("*********************************")

    palavra_secreta = "banana"

    letras_certas = ["_", "_", "_", "_", "_", "_"]

    enforcou = False
    acertou = False
    print("Dica: {} letras! ".format(len(letras_certas)))
    while(not enforcou and not acertou):
        chute = input("Chute uma letra: ")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                print("Encontrei a letra {} na posição {}.".format(letra,index))
                letras_certas[index] = letra

            index = index + 1
        #else:
        #    print("A letra {} não existe na palavra.".format(chute))
        print("A palavra é {}.".format(letras_certas))

        letras_faltando = str(letras_certas.count('_'))
        print('Ainda faltam acertar {} letras'.format(letras_faltando))

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()