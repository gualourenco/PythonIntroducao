import forca_alura
import advinhacao_alura

print('***********************************************')
print('         !!!!Bem vindo aos nossos jogos!!!!      ')
print('***********************************************')

def escolher_jogo():
    print('Escolha um jogo:')
    print('(1)  Forca  \n(2) Adivinhação\n')

    jogo = input('Qual vamos jogar?')
    jogo = jogo.strip()

    if jogo.isdecimal() and jogo == '1' :
        jogar_forca()

    elif  jogo.isdecimal() and jogo == '2':
        jogar_advinhacao()

    else:
        esse_nao()

def jogar_forca():
    print('Jogando Forca')
    forca_alura.jogar_forca()

def jogar_advinhacao():
    print('Jogando Advinhação')
    advinhacao_alura.jogar_advinhacao()

def esse_nao():
    print("Hummmmmm.......\nAinda não temos essa opção")
    print('\nVamos voltar à seleção de jogos ;)')
    return escolher_jogo()

if __name__ == '__main__':
    escolher_jogo()
