import random

print("***********************************")
print("Bem vindo ao jogo de adivinhação!")
print("***********************************")

numero_secreto = random.randrange(1,101)
print(numero_secreto)

total_de_tentativas = 3
rodada = 1

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
        print("Você acertou!")
        break
    else:
        if(maior):
            print("Você errou! O seu chute foi maior que o número secreto.")
        #elif = o else if
        elif(menor):
            print("Você errou! O seu chute foi menor que o número secreto.")
    rodada = rodada + 1
print("Fim do jogo")
