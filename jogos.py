import forca
import advinhacao

def escolhe_jogo():

    print("*********************************")
    print("********Escolha seu jogo!********")
    print("*********************************")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual o jogo? "))

    if(jogo==1):
        print("Jogando o jogo da Forca!")
        forca.jogar()
    elif(jogo==2):
        print("Jogando o jogo da Adivinhação!")
        advinhacao.jogar()
    else:
        print("Opção Inválida!")

if(__name__ == "__main__"):
    escolhe jogo()