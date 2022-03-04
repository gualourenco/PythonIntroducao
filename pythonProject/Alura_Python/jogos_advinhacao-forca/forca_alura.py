import random

def jogar_forca():

    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()
    letras_certas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_certas)

    enforcou = False
    acertou = False
    erro = 0

# enquanto (True)
    while not enforcou and not acertou:

        chute = insere_chute()

        if chute in palavra_secreta:
            marca_chute_correto(palavra_secreta, chute, letras_certas)
        else:
            erro += 1
            desenha_forca(erro)
        enforcou = erro == 6
        acertou = '_' not in letras_certas
        print(letras_certas)

    if acertou:
        final_venceu()
    else:
        final_perdeu(palavra_secreta)

    print('Fim de Jogo')

def imprime_mensagem_abertura():
    print('**********************************')
    print('     ***  Jogo da Forca!     ***  ')
    print('**********************************')

def carrega_palavra_secreta():
    arquivo_palavras = open('palavras.txt', 'r')
    lista_frutas = []

    for fruta in arquivo_palavras:
        fruta = fruta.strip()
        lista_frutas.append(fruta)

    arquivo_palavras.close()

    aleatorio = random.randrange(0, len(lista_frutas))
    palavra_secreta = lista_frutas[aleatorio].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ['_' for letra in palavra]

def insere_chute():
    chute = input("Qual a letra?: ")
    chute = chute.strip().upper()
    return chute

def marca_chute_correto(palavra_secreta, chute, letras_certas):
    posicao = 0
    for caractere in palavra_secreta:
        if (chute == caractere):
            letras_certas[posicao] = caractere  # cada letra certa armazena na sua posição dentro da lista
        posicao += 1

def final_perdeu(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("      _______________         ")
    print("     /               \        ")
    print("    /                 \       ")
    print("  //                   \/\    ")
    print("  \|   XXXX     XXXX   | /    ")
    print("   |   XXXX     XXXX   |/     ")
    print("   |   XXX       XXX   |      ")
    print("   |                   |      ")
    print("   \__      XXX      __/      ")
    print("     |\     XXX     /|        ")
    print("     | |           | |        ")
    print("     | I I I I I I I |        ")
    print("     |  I I I I I I  |        ")
    print("     \_             _/        ")
    print("       \_         _/          ")
    print("         \_______/            ")

def desenha_forca(erro):
    print("  _______     ")
    print(" |/      |    ")

    if(erro == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erro == 2):
        print(" |      (_)   ")
        print(" |       |    ")
        print(" |       |    ")
        print(" |            ")

    if(erro == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |       |    ")
        print(" |            ")

    if(erro == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erro == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if(erro == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")


    print(" |            ")
    print("_|___         ")
    print()

def final_venceu():
    print("Parabéns, você ganhou!")
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

if(__name__=='__main__'):
    jogar_forca()