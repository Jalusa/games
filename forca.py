import random

def jogar():

    iniciando()

    palavra_secreta = carrega_palavra_secreta()

    letras_certas = ["_" for letras in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print("Dica: {} letras! ".format(len(letras_certas)))

    while (not enforcou and not acertou):

        chute = input("Chute uma letra: ")
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    # print("Encontrei a letra {} na posição {}.".format(letra,index))
                    letras_certas[index] = letra
                index += 1
        else:
            erros += 1

        if ("_") not in letras_certas:
            print("Você acertou! A palavra secreta é {}.".format(palavra_secreta))
            break

        enforcou = erros == 6
        if (enforcou):
            print("Você perdeu. Suas chances acabaram!")
            break

        print("A palavra é {}.".format(letras_certas))
        chances = 6 - erros
        letras_faltando = str(letras_certas.count('_'))
        print('Ainda faltam acertar {} letras. Você tem {} chances de errar!'.format(letras_faltando, chances))

    print("Fim do jogo")


if (__name__ == "__main__"):
    jogar()


def iniciando():
    print("*********************************")
    print("***Bem vindo ao jogo de Forca!***")
    print("*********************************")

 def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.apped(linha)

    arquivo.close()
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()