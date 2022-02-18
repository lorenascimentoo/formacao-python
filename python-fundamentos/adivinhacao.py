import random

def jogar():

    print("***********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("***********************************")

    #Gera o numero secreto aleatoriamente
    numero_secreto = random.randrange(1,101)
    print(numero_secreto)

    total_de_tentativas = 0

    print("(1) FÁCIL (2) MÉDI0 (3) DIFÍCIL")
    nivel = int(input("Digite o nível: "))
    # A partir da entrada do usuario define o numero de tentativas
    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    rodada = 1
    pontos = 1000

    for rodada in range (1,total_de_tentativas+1):
        #interpolação de string
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute_str = input("Digite um numero entre 1 e 100: ")
        print("Você digitou: ", chute_str)
        chute = int(chute_str)

        if( chute < 1 or chute > 100):
            print("Você deve digitar um numero entre 1 e 100!")
            #para que vá para a próxima iteração sem executar o restante do código e ele não saia do laço
            continue

        acertou = chute == numero_secreto
        maior = chute>numero_secreto
        menor = chute<numero_secreto

        if(acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            pontos_perdidos = abs(numero_secreto-chute)
            pontos = pontos - pontos_perdidos
            if(maior):
                print("Você errou! O seu chute foi maior que o número secreto.")
                if(rodada == total_de_tentativas):
                    print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))
            #elif = o else if
            elif(menor):
                print("Você errou! O seu chute foi menor que o número secreto.")
                if(rodada == total_de_tentativas):
                    print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))
        rodada = rodada + 1
    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()