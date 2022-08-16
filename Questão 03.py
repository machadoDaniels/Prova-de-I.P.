# Aluno: Daniel Machado Pedrozo
# Matrícula: 202202434


import numpy as np
'''Legenda:
    ~ : mar/oceano
    ^,v,<,>: proa ou popa do navio(Partes de frente ou de trás) - Suas Delimitaçôes
    H, =: corpo do navio'''


def clear(txt, limp=False):  # limpa o console para que um jogador não veja o jogo do adversário
    # Criando dois "tipos" de clear() dependendo na necessidade, o primeiro, limpa o console primeiro, o segundo, mostra o txt e espera o usuário digitar alguma tecla
    if limp is True:
        input("------APERTE ENTER PARA LIMPAR O CONSOLE------")
        print("\n" * 130)
        input(txt)
    else:
        input(txt)
        print("\n" * 130)


def linha(x):  # Desenha linha para melhorar estética
    print('-' * x)


def campo(msg):  # Desenha o campo de bataha de um dos jogadores ou das visões que possuem do campo adversário
    for l in msg:
        print(end='| ')
        for c in l:
            if c in '<=>v^H':  # Colocando cores para melhorar visualização dos elementos
                c = f"\033[33m{c}\033[m"  # amarelo para os barcos
            elif c == '~':
                c = f"\033[34m{c}\033[m"  # azul para o oceano
            elif c == 'x':
                c = f"\033[31m{c}\033[m"  # vermelho para marcar os tiros
            if c in '<=' and c != l[-1]:
                print(c, end='   ')
            else:
                print(f"{c}", end=' | ')
        print()


def campo_tot(msg):  # Desenha o campo de batalha do jogador, e a visão que possui do campo de seu inimo acima
    if msg == 'jogador1':
        campo(visao_jogador_1)
        linha(42)
        campo(jogador1)
    else:
        campo(visao_jogador_2)
        linha(42)
        campo(jogador2)


# Gerando matrizes para definir o campo de batalha de cada jogador e as visões que possuem de seu adverário.
jogador1 = np.full((6, 10), str('~'))
jogador2 = np.full((6, 10), str('~'))
visao_jogador_1 = np.full((6, 10), str('~'))
visao_jogador_2 = np.full((6, 10), str('~'))

# Definindo os Navios do jogador 1
navio5l = 0
navio5c = 0
jogador1[navio5l: navio5l + 5, navio5c] = ['^', 'H', 'H', 'H', 'v']  # Navio de tamanho 5u.a.
navio4l = 0
navio4c = 1
jogador1[navio4l: navio4l + 4, navio4c] = ['^', 'H', 'H', 'v']  # Navio de tamanho 4u.a.
navio3l = 0
navio3c = 2
jogador1[navio3l: navio3l + 3, navio3c] = ['^', 'H', 'v']  # Navio de tamanho 3u.a.

# Definindo os Navios jogador 2:

navio5l_jog2 = 0
navio5c_jog2 = 0
jogador2[navio5l_jog2: navio5l_jog2 + 5, navio5c_jog2] = ['^', 'H', 'H', 'H', 'v']
navio4l_jog2 = 0
navio4c_jog2 = 1
jogador2[navio4l_jog2: navio4l_jog2 + 4, navio4c_jog2] = ['^', 'H', 'H', 'v']
navio3l_jog2 = 0
navio3c_jog2 = 2
jogador2[navio3l_jog2: navio3l_jog2 + 3, navio3c_jog2] = ['^', 'H', 'v']


# Começando - Jogador 1:

print("\033[1;35mCAMPO DE BATALHA - JOGADOR 1:\033[m")
campo_tot('jogador1')
if str(input("Você quer alterar a posição de seus navios[s/n]? ")) == 's':

    # Reformatando o campo do jogador 1 - Redefinindo as posições dos navios:

    jogador1 = np.full((6, 10), str('~'))
    formato_navio5 = str(input("Você quer seu navaio 5 na vertical ou na horizontal[v/h]? "))  # Definindo o sentido do navio para alterar linha ou voluna dependendo do resultado:
    navio5l = int(input('Linha onde começa seu navio de tamanho 5:'))
    navio5c = int(input('Coluna onde começa seu navio de tamanho 5:'))
    if formato_navio5 in 'Vv':
        jogador1[navio5l: navio5l + 5, navio5c] = ['^', 'H', 'H', 'H', 'v']  # Colocando o navio na vertical, na posição definida pelo jogador.
    else:
        jogador1[navio5l, navio5c: navio5c + 5] = ['<', '=', '=', '=', '>']  # Colocando o navio na horizontal, na posição definida pelo jogador.
    campo_tot('jogador1')

    #  Repetindo o processo para o navio 4
    formato_navio4 = str(input("Você quer seu navio 4 na vertical ou na horizontal[v/h]? "))
    navio4l = int(input('Linha onde começa seu navio de tamanho 4:'))
    navio4c = int(input('Coluna onde começa seu navio de tamanho 4:'))
    if formato_navio4 in 'Vv':
        jogador1[navio4l: navio4l + 4, navio4c] = ['^', 'H', 'H', 'v']
    else:
        jogador1[navio4l, navio4c: navio4c + 4] = ['<', '=', '=', '>']
    campo_tot('jogador1')

    #  Repetindo o processo para o navio 3
    formato_navio3 = str(input("Você quer seu navio 3 na vertical ou na horizontal[v/h]? "))
    navio3l = int(input('Linha onde começa seu navio de tamanho 3:'))
    navio3c = int(input('Coluna onde começa seu navio de tamanho 3:'))
    if formato_navio3 in 'Vv':
        jogador1[navio3l: navio3l + 3, navio3c] = ['^', 'H', 'v']
    else:
        jogador1[navio3l, navio3c: navio3c + 3] = ['<', '=', '>']
    campo_tot('jogador1')


clear("APERTE ENTER PARA MOSTRAR O CAMPO DO JOGADOR 2", limp=True)

# Comçando - Jogador 2:

print("\033[1;35mCAMPO DE BATALHA - JOGADOR 2:\033[m")
campo_tot('jogador2')
if str(input("Você quer alterar a posição de seus navios[s/n]? ")) == 's':

    # Reformatando o campo do jogador 2, assim como já comentado para o jogador 1:

    jogador2 = np.full((6, 10), str('~'))
    formato_navio5 = str(input("Você quer seu navaio 5 na vertical ou na horizontal[v/h]? "))
    navio5l_jog2 = int(input('Linha onde começa seu navio de tamanho 5:'))
    navio5c_jog2 = int(input('Coluna onde começa seu navio de tamanho 5:'))
    if formato_navio5 in 'Vv':
        jogador2[navio5l_jog2: navio5l_jog2 + 5, navio5c_jog2] = ['^', 'H', 'H', 'H', 'v']
    else:
        jogador2[navio5l_jog2, navio5c_jog2: navio5c_jog2 + 5] = ['<', '=', '=', '=', '>']
    campo_tot('jogador2')

    formato_navio4 = str(input("Você quer seu navio 4 na vertical ou na horizontal[v/h]? "))
    navio4l_jog2 = int(input('Linha onde começa seu navio de tamanho 4:'))
    navio4c_jog2 = int(input('Coluna onde começa seu navio de tamanho 4:'))
    if formato_navio4 in 'Vv':
        jogador2[navio4l_jog2: navio4l_jog2 + 4, navio4c_jog2] = ['^', 'H', 'H', 'v']
    else:
        jogador2[navio4l_jog2, navio4c_jog2: navio4c_jog2 + 4] = ['<', '=', '=', '>']
    campo_tot('jogador2')

    formato_navio3 = str(input("Você quer seu navio 3 na vertical ou na horizontal[v/h]? "))
    navio3l_jog2 = int(input('Linha onde começa seu navio de tamanho 3:'))
    navio3c_jog2 = int(input('Coluna onde começa seu navio de tamanho 3:'))
    if formato_navio3 in 'Vv':
        jogador2[navio3l_jog2: navio3l_jog2 + 3, navio3c_jog2] = ['^', 'H', 'v']
    else:
        jogador2[navio3l_jog2, navio3c_jog2: navio3c_jog2 + 3] = ['<', '=', '>']
    campo_tot('jogador2')


clear("------APERTE ENTER PARA COMEÇAR O JOGO------")
#  O Jogo Começa
cont = 0
while True:
    cont += 1
    print(f"{'-'*16} RODADA {cont} {'-'*16}")  # Separa o jogo rodadas, nas quais cada jogador tem 1 turno
    print(f"JOGADOR 1, SEU TURNO")
    ltiro1 = int(input('Linha do seu tiro: '))  # Jogador define a linha e coluna de onde quer atirar
    ctiro1 = int(input('Coluna do seu tiro: '))
    if jogador2[ltiro1, ctiro1] in '><=v^H':  # Caso haja um navio na posição do tiro ele, o computador informa
        print("VOCÊ ACERTOU UM NAVIO!!")
    else:
        print("NENHUM NAVIO FOI ATINGIDO!!")
    visao_jogador_1[ltiro1, ctiro1] = 'x'  # Coloca um x no lugar da posição atingida para marcar o tiro, tanto no campo do jogador adversário quanto na visão do jogador que atirou.
    jogador2[ltiro1, ctiro1] = 'x'
    campo_tot('jogador1')
    # Quando todas as partes dos navios são trocadas por x, significa que a partida acabou e dá um break no loop.
    if '<' not in jogador2 and '>' not in jogador2 and '=' not in jogador2 and 'v' not in jogador2 and 'H' not in jogador2 and '^' not in jogador2:
        print(f"\033[32m{'-=' * 10} FIM DE JOGO {'-=' * 10}")
        print("O JOGADOR 1 É O VENCEDOR !!!!!")
        break
    clear("APERTE ENTER PARA FINALIZAR SEU TURNO")
    # Repete o processo já comentado para o jogador 2
    print(f"JOGADOR 2, SEU TURNO")
    ltiro2 = int(input('Linha do seu tiro: '))
    ctiro2 = int(input('Coluna do seu tiro: '))
    if jogador1[ltiro2, ctiro2] in '><=v^H':
        print("VOCÊ ACERTOU UM NAVIO!!")
    else:
        print("NENHUM NAVIO FOI ATINGIDO!!")
    visao_jogador_2[ltiro2, ctiro2] = 'x'
    jogador1[ltiro2, ctiro2] = 'x'
    campo_tot('jogador2')
    if '<' not in jogador1 and '>' not in jogador1 and '=' not in jogador1 and 'v' not in jogador1 and 'H' not in jogador1 and '^' not in jogador1:
        print(f"\033[32m{'-=' * 8} FIM DE JOGO {'-=' * 8}")
        print("O JOGADOR 2 É O VENCEDOR !!!!!")
        break
    clear("APERTE ENTER PARA FINALIZAR SEU TURNO")
