import forca
import adivinhacao

def escolher_jogo():
    print("***********************************")
    print("*********Sistema de jogos**********")
    print("***********************************")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Digite o jogo escolhido: "))

    if(jogo ==1):
        print("Jogando forca")
        forca.jogar()
    elif(jogo==2):
        print("Jogando adivinhação")
        adivinhacao.jogar()

if(__name__ == "__main__"):
    escolher_jogo()