import random
import time

matriz_jogo = [[' ' for i in range(3)] for j in range(3)]


def tabuleiro(matriz_jogo):
    for i, linha in enumerate(matriz_jogo):
        print(f'{linha[0]}  | {linha[1]} | {linha[2]}')
        if i < 2:
            print('---+---+---')
tabuleiro(matriz_jogo)

def marcar_jogador():
    while True:
        try:
            perg_linha = int(input('\nDigite uma linha: ')) - 1

            perg_coluna = int(input('Digite uma coluna: ')) - 1
            
            if 0 <= perg_linha <= 2 and 0 <= perg_coluna <= 2:

                if matriz_jogo[perg_linha][perg_coluna] == ' ':
                    matriz_jogo[perg_linha][perg_coluna] = 'X'
                    break
                else:
                    print('\nPosição já ocupada\n')
                    tabuleiro(matriz_jogo)
            else:
                    print('\nDigite um número de 1 a 3')
        except ValueError:
            print('\nDigite uma entrada válida')
def marcar_maquina():
        while True:
            linha_maquina = random.randint(0, 2)
            coluna_maquina = random.randint(0, 2)
            if matriz_jogo[linha_maquina][coluna_maquina] == ' ':
                matriz_jogo[linha_maquina][coluna_maquina] = 'O'
                break
def verificar_vitoria(simbolo):
    #Linha
    for linha in matriz_jogo:
        if linha.count(simbolo) == 3:
            return True
    #Coluna
    for coluna in range(3):
        if matriz_jogo[0][coluna] == simbolo and matriz_jogo[1][coluna] == simbolo and matriz_jogo[2][coluna] == simbolo:
            return True
    #Diagonal
    if matriz_jogo[0][0] == simbolo and matriz_jogo[1][1] == simbolo and matriz_jogo[2][2] == simbolo:
        return True
    if matriz_jogo[0][2] == simbolo and matriz_jogo[1][1] == simbolo and matriz_jogo[2][0] == simbolo:
        return True
    
def empate():
    for linha in matriz_jogo:
        if ' ' in linha:
            return False
    return True

# 1 é o jogador e 2 a maquina(ISSO VAI DEFINIR QUEM VAI JOGAR PRIMEIRO)
primeiro = random.randint(1,2)

while True:
    if primeiro == 1:
        marcar_jogador()

        print('\nSua Jogada:\n')

        tabuleiro(matriz_jogo)

        if verificar_vitoria('X'):
            print('\nParabéns, você ganhou!\n')
            break

        if empate():
            print('\nEmpate!\n')
            break

        primeiro = 2

    if primeiro == 2:
        print('\nVez da máquina...\n')
        time.sleep(1)

        marcar_maquina()

        tabuleiro(matriz_jogo)
        
        if verificar_vitoria('O'):
            print('\nVocê Perdeu!\n')
            break

        if empate():
            print('\nEmpate!\n')
            break

        primeiro = 1
