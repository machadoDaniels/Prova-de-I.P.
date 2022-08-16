# Aluno: Daniel Machado Pedrozo
# Matrícula: 202202434


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
