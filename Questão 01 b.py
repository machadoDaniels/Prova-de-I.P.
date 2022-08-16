# Aluno: Daniel Machado Pedrozo
# Matrícula: 202202434


import numpy as np
from random import randint


def mostraarray(arr):  # Mostra a matriz formatada
    cont = 0
    for l in arr:
        print(f'{cont:2})', end= ' ')
        cont += 1
        for e in l:
            print(f'{e}', end='  ')
        print()

# O começa com uma palavra na vertical e uma na horizontal para evitar erros se o p
palavras_v = ['programação']  # palavras que serão colocadas na vertical no caça palavras
palavras_h = ['aprovado']  # palavras que serão colocadas na horizontal no caça palavras

# Começa com uma palavra na vertical e uma na horizontal para evitar erros se o usuário colocar somente uma palavra


while True:  # adiciona a quantidade de palavras que o usuário quiser até que receba o comando de parar
    palavra = str(input("Adicione uma palavra: "))
    if str(input(f"Você quer a palavra na vertical ou horizontal[v/h]? ")) in 'vV':
        palavras_v.append(palavra)
    else:
        palavras_h.append(palavra)
    if str(input("Quer continuar[s/n]? ")) in 'Nn':
        break

max_palavra_v = max_palavra_h = 0

# Para definir o numero de colunas em função da quantidade e o do tamanho das palavras colocadas
for c in palavras_v:
    if len(c) > max_palavra_v:
        max_palavra_v = len(c)

# Para definir o numero de linhas em função da quantidade e o do tamanho das palavras colocadas
for i in palavras_h:
    if len(i) > max_palavra_h:
        max_palavra_h = len(i)

# Gera a matriz que formará o caça palavras, primeiramente, com todos elementos = 'o':
cp = np.full((max_palavra_v + len(palavras_h), max_palavra_h + len(palavras_v)), str('o'))
mostraarray(cp)

# O usuário define a linha e a coluna de cada palavra na vertical
for p in palavras_v:
    l = int(input(f"Em qual linha você quer '{p}'? "))
    c = int(input(f"Em qual coluna você quer '{p}'? "))
    p = p.upper()  # Coloca a palavra em letras maiúsculas
    p = list(p)  # Transforma a palavra em uma lista para que possa tranformar em um array
    p = np.array(p)  # Transforma a lista em um array para facilitar seu manuseio
    cp[l: l + len(p), c] = p  # Insere a palavra no lugar selecionado pelo usuário
    mostraarray(cp)

# O usuário define a linha e a coluna de cada palavra na horizontal
for p in palavras_h:
    l = int(input(f"Em qual linha você quer '{p}'? "))
    c = int(input(f"Em qual coluna você quer '{p}'? "))
    p = p.upper()
    p = list(p)
    p = np.array(p)
    cp[l, c: c + len(p)] = p
    mostraarray(cp)

# Troca os elementos da matriz que se mantiveram como 'o', ou seja, não receberam letra de nenhuma palavra inserida.
for l in range(0, max_palavra_v + len(palavras_h)):
    for c in range(0, max_palavra_h + len(palavras_v)):
        if cp[l, c] == str('o'):
            cp[l, c] = chr(randint(ord('A'), ord('Z')))  # Substitui as letras 'o' por letraz randomizadas do alfabeto.


print(f"{'-'* 15}CAÇA PALAVRAS{'-'* 15}")
mostraarray(cp)



'''
# solução alternativa - baseda nos algoritimos que dados pela questão

from random import randint
s = "programacao"
s = list(s)  # Tranformando a palavra em uma lista para que possamos alterar cada letra individualmente.
for letra in s:
    print(letra)
maior = 'p'
while True:
    f = str(input("Qual palavra você quer adicionar no caça palavras? "))
    c = f[0]  # Primeira letra da palavra recebida

    # Descobrindo as posições onde a letra foi encontrada.
    lst = []
    for pos, char in enumerate(s):
        if char == c:
            lst.append(pos)
    print(f"Posições novas onde foi encontrada a letra '{f[0]}':", lst)

    # Se a primeira letra da palavra recebida não estiver em 'programação', colocamos a palavra no final da lista
    #  Caso contrário, randomiza a posição entre as possibilidades encontradas na linha 15 do código.
    if len(lst) == 0:
        s.append(f)
    else:
        lposi = lst[randint(0, len(lst) - 1)]
        x = 0
        s[lposi] = f
    for letra in s:
        print(letra)
    if len(f) > len(maior):
        maior = f
    # Usuário define a quantidade de palavras que serão colocadas e quando ele vai parar.
    if str(input("Quer continuar? ")) in 'Nn':
        break
# Gera uma matriz com quantidade de linhas definidas pela 'len' da lista principal(s), e com quant. de colunas definidas pelo 'len' da maior palavra colocada pelo o usuário.
for letra in s:
    if len(letra) == len(maior):
        for i in letra:
            print(i, end=' ')
    else:
        for c in range(len(maior) - len(letra)):  # Descobre a quantidade de letras em cada linha, dependendo do tamanho da palavra.
            letra += chr(randint(ord('a'), ord('z')))  # Completa a linha com letras aleatórias
        for i in letra:
            print(i, end=' ')
    print()
'''
