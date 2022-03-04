import random #random é um módulo a ser importado para o código
# a função randrange limita a aleatoriedade entre o primeiro e o segundo parametro
# a função random.random() gera um numero aleatório em float, de 0.0 à 1

def jogar_advinhacao():

    print('**********************************')
    print('    *** Jogo de advinhação! ***    ')
    print('**********************************')

    numero_secreto = random.randrange(1, 101)
   # print(numero_secreto)
    tentativas     = 0
    pontos         = 1000

    print('Qual o nível de dificuldade?')
    print("(1) Fácil: 20 rodadas (2) Médio: 10 rodadas (3) Difícil: 5 rodadas")

    nivel = int(input("Defina o nível:  "))

    if (nivel == 1):
        tentativas = 20
    elif (nivel ==2):
        tentativas = 10
    else:
        tentativas = 5


    for rodada in range(1, tentativas +1):
        print("Rodada: {} de: {}".format(rodada, tentativas))

        chute_str = input('Digite o seu número: ')
        print('Você digitou ', chute_str)

        chute_int = int(chute_str)
    #    print(type(chute_int))

        if (chute_int < 1 or chute_int > 100):
            print('Você deve digitar um número entre 1 e 100!')
            continue

        acertou = numero_secreto == chute_int
        menor   = numero_secreto > chute_int
        maior   = numero_secreto < chute_int

        if (acertou):
            print('Acertou!!!')
            #print(type(acertou))
            print("Você fez {} pontos!".format(pontos))
            break
        else:
            if (menor):
                print('Errou! Seu número é menor que o número secreto')
              #  print(type(menor))
                if (rodada == tentativas):
                    print('Acabaram suas tentativas. \nO número secreto era: {} \n Você fez {} pontos! \n.'
                          .format(numero_secreto, pontos))

            elif (maior):
                print('Errou! Seu número é maior que o número secreto')
               # print(type(maior))
                if (rodada == tentativas):
                    print('Acabaram suas tentativas. \nO número secreto era: {} \n Você fez {} pontos! \n.'
                          .format(numero_secreto, pontos))
            pontos_perdidos = abs(numero_secreto - chute_int) #Ex: 40 - 20 = 20
            pontos = pontos - pontos_perdidos



    print('fim do jogo')
if(__name__=="__main__"):
    jogar_advinhacao()
