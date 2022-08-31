# Aluno: Daniel Machado Pedrozo
# Matrícula: 202202434

'''EXTRA - Você começou a estudar numpy exercitando no colab queoprofessor Leonardo enviou em sala, gostou muito e quis propor umaquestão aceitando o desafio usando o que aprendeu. Desenvolveuumaquestão e inclusive que apresentou uma aplicação prática unindo outroconhecimento ou hobby que possui apresentando a solução comumcódigobemcomentado. (valor 1.0)
[obs.: o uso agregado ou a substituição por outro framework estudado está liberadopor ser uma questão extra. Exemplo: Desenvolvimento usando umconhecimentoouhobby usando um framework de IA que tenha visto nos videos de frameworks das
turmas anteriores. ]'''

''' Um lojista precisa ter um controle melhor de seus gastos, por isso, te contratou para fazer um programa que
ajude calcular seu custo, preço de venda e lucro do primeiro trimestre do ano e gera um gráfico de barras para analisar
o crescimento ou descresimento das vendas. '''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


n = int(input("Quantidade de produtos da loja: "))
mes = np.array(['Jan.', 'Fev.', 'Mar.'])  # primeiro trimestre que vamos analisar
valores = np.array(['Custo', 'Preço de Venda', 'Lucro'])
valores_trim = ['Custo Trim.', 'Preço de Venda Trim.', 'Lucro Trim.']
produtos = []
n_vendas = np.zeros([3, n])
custo = np.zeros([n, 3])

for c in range(0, n):
    produtos.append(str(input(f"Produto {c}: ")))  # Pede o nome de cada um dos produtos

for l in range(0, 3):  # Monta uma matriz com a quantidade de cada produto que foi vendida em cada mes
    for e in range(0, n):
        n_vendas[l, e] = float(input(f"Quantidade de {produtos[e]} vendididas em {mes[l]}:"))

for l in range(0, n):  # Monta uma matriz com o custo, preco de venda e lucro de cada produto, 1 produto vendido.
    for e in range(0, 3):
        if valores[e] == 'Lucro':
            custo[l, e] = custo[l, e - 1] - custo[l, e - 2]
        else:
            custo[l, e] = float(input(f"{valores[e]} de {produtos[l]}:"))

# Cria uma tabela, devidadamente formatda, para mostrar a quantidade de cada um dos produtos que foi vendida em cada mes

df_n_vend = pd.DataFrame(np.array(n_vendas),
                   columns=produtos, index=mes)
print(df_n_vend)

# Cria uma tabela, devidadamente formatda, para mostrar o custo, preço de venda e lucro a cada produto vendido.

df_cust = pd.DataFrame(np.array(custo),
                   columns=valores, index=produtos)
print(df_cust)


# Multiplando a matriz com as quantidades de vendas pela matriz com os custos, preço e lucro, obtemos uma nova matriz, com os valores trimestrais de custo, preço de venda e lucro.

tot = np.dot(n_vendas, custo)
df_tot = pd.DataFrame(np.array(tot),
                   columns=valores_trim, index=mes)
print(df_tot)

df_n_vend.plot(kind='bar')
plt.show()
