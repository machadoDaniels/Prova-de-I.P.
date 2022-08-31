# Aluno: Daniel Machado Pedrozo
# Matrícula: 202202434

'''4 - Um colega do BIA da turma 2021, te enviou um código pedindo para
que você olhasse e o ajudasse a corrigir o mesmo. (valor 2.0)
Segue o código:

import random

def ordenacao_selecao(A):

# Verificar o tamanho dinamicamente do vetor A.
cont = 0
while true:
if A[cont] == null:
n = cont
# Percorre o arranjo A.
for i in range(n):
# Encontra o elemento mínimo em A.
minimo = i
# Coloca o elemento mínimo na posição correta.
#???? (como posso colocar ele na posição corretapara a saída?)
A = random.sample(range(-10, 10), 10)
print("Arranjo não ordenado: ", A)
ordenacao_selecao(A)
print("Arranjo ordenado:", A)

A) Explique qual foi o erro e corrija o código para o colega.
B) Como você estava aprendendo sobre gráficos, plotou os valores emumgráficodebarras para mostrar ambas as barras
 uma desordenada e outra ordenada.
'''


import random
import pandas as pd
import matplotlib.pyplot as plt


def mostrarvalores(lista):  # Mostra os valores numa tabela e num gráfico de barras
    valores = []
    cont = 0
    for valor in lista:  # Adiciona os elementos da lista em tuplas, nomeando cada 1, e adiciona cada tupla na lista "valores" criada.
        valores.append((f'Valor {cont}', valor))
        cont += 1

    df = pd.DataFrame(valores, columns=('Name', 'Valores'))  # Organiza os valores em uma tabela

    print(df)

    df.plot(kind='bar')  # Coloca os valores da tabela num gráfico de barras
    plt.show()  # Mostra o gráfico de barras criado


def ordenacao_selecao(a):  # Poderia trocar pela funçâo ".sort()", que ordena na ordem crescente automaticamente.
    # Verificar o tamanho dinamicamente do vetor A.
    cont = 0
    while True:  # Pode ser trocado pela função "len()" que lê a quantidade de elemetos na lista
        cont += 1  # Colocando o contador dentro do loop
        # O códgio veio estava com o nome 'null', indefinido, vamos trocá-la para que o loop termine quando o elemento com índice do contador seja o último elemenento da lista.
        if a[cont] == a[-1]:
            cont += 1  # O contador anterior não estava na posiçäo correta
            n = cont
            break  # No código anterior, faltava o 'break' para acabar com o loop while
    # Percorre o arranjo a.
    for i in range(n):
        # Encontra o elemento mínimo em a.
        minimo = a[i]  # O código anterior recebia minimo como 'i', também é possível fazer dessa forma
        for j in range(i + 1, n):
            # Trocando o "A[minimo]" por "minimo".
            if minimo > a[j]:
                minimo = a[j]
                # Invertendo as posiçoes do elemento comparado com um que seja menor que ele.
                a[i], a[j] = a[j], a[i]
                # Coloca o elemento mínimo na posição correta.


A = random.sample(range(-10, 10), 10)  # Cria lista com 10 valores aleatórios
print("Arranjo não ordenado: ", A)


mostrarvalores(A)

ordenacao_selecao(A)

print("Arranjo ordenado:", A)

mostrarvalores(A)
