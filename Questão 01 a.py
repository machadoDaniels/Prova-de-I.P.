# Aluno: Daniel Machado Pedrozo
# Matrícula: 202202434

'''- Você recebeu um desafio de um colega do BIA que te perguntou comopoderia criar uma caça palavras em python, contendo no mínimo 3 palavras
imputadas pelo usuário. Você dele ler um conjunto de palavras e gerar umcaça
palavras. Um colega do BIA de 2020 te enviou um código, para ajudá-lo.(valor 2.0)

A) Explique os algoritmos que o seu colega te apresentou
B) Desenvolva a sua solução e explique'''


def main():
    s = "programacao"  # Palavra base para o caça palavras
    f = "aprovado"  # Palavra que será adicionada ao caça palavras
    c = f[0]  # Pegando a primeira letra e vendo sua coincidência com as letras da palavra base
    # quantas letras existem e em que posições?
    lst = []
    for pos,char in enumerate(s):  # Acha as possíveis posições para encaixar a palavra 'aprovado'
        if char == c:
            lst.append(pos)
    print("posições onde foi encontrada a letra 'a'", lst)

    #vamos imprimir a letra usando a posicao 2 da lista
    lposi = lst[1]
    x = 0
    for l in s:  # imprime letra por letra, trocando o segundo 'a' por 'aprovado'
        if x == lposi:
            print(f)
        else:
            print(l)
        x += 1


main()
