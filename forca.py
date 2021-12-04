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

        chute = chute_jogador()

        if (chute in palavra_secreta):
            marca_chute_correto(chute,letras_certas,palavra_secreta)
        else:
            erros += 1
            desenha_forca(erros)

        if ("_") not in letras_certas:
            imprime_mensagem_vencendor()

        enforcou = erros == 7
        if (enforcou):
            imprime_mensagem_perdedor(palavra_secreta)

        print("A palavra é {}.".format(letras_certas))
        chances = 6 - erros
        letras_faltando = str(letras_certas.count('_'))
        print('Ainda faltam acertar {} letras. Você tem {} chances de errar!'.format(letras_faltando, chances))

    print("Fim do jogo")

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
    return palavra_secreta

 def chute_jogador():
     chute = input("Chute uma letra: ")
     chute = chute.strip().upper()
     return chute

def marca_chute_correto(chute, letras_certas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_certas[index] = letra
        index += 1

def imprime_mensagem_vencedor():
    print("Você acertou! A palavra secreta é {}.".format(palavra_secreta))
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
    break

def imprime_mensagem_perdedor(palavra_secreta):
    print("Você perdeu. Suas chances acabaram!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
    break

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if (__name__ == "__main__"):
    jogar()
