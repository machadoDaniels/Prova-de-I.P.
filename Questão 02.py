# Aluno: Daniel Machado Pedrozo
# Matrícula: 202202434
'''2 - Você ingressou em uma fase de um projeto de pesquisa no CEIA, nesseprojeto você irá auxiliar na análise de dados
médicos para umplano de saúde. Foi levantada a planilha de dados a partir da mineração dos dados daoperadora junto com
eus médicos, (planilha publicado no linkhttps://bit.ly/3RhcnGL).'''

import pandas as pd
xls = pd.read_excel('dadosmedicossaude.xlsx')
lista = xls.values.tolist()
tot_imc = []
soma_imc = maior_imc_risco = ind_maior = ind_menor = 0
menor_imc_risco = 999
for paciente in lista:  # analisando cada paciente individualmente
    imc = paciente[2] / paciente[1] ** 2  # calculando o imc de cada paciente(peso/altura^2).
    paciente.append(imc)  # adicionando o imc junto da ficha de cada paciente
    soma_imc += imc  # descobrindo a soma de todos IMCs
    tot_imc.append(imc)  # criando uma lista com todos IMCs para descobrir a faixa em que se encontram
    # vamos considerar que o risco de vida está associado diretamente com a baixa de vitaminas ou ao risco cardíaco e com um imc alto demais ou baixo demais.
    if paciente[3] == 'Risco' or paciente[4] == 'Baixa de vitaminas':  # analisando somente os pacientes que possuem baixa de vitaminas ou risco cardíaco, descobriremos o maior e o menor imc entre eles.
        if imc > maior_imc_risco:
            ind_maior = lista.index(paciente)  # descobrindo o índice da lista em que se encontra.
            maior_imc_risco = imc
        if imc < menor_imc_risco:
            ind_menor = lista.index(paciente)
            menor_imc_risco = imc

# Coloca lista em dataframe para melhorar análise de dados e adiciona nova coluna com os imcs de cada paciente.
df = pd.DataFrame(lista, columns=('nome do paciente anonimizado', 'altura', 'peso', 'risco cardíago', 'status de vitaminas', 'imc'))

print(df)

media_imc = soma_imc / len(lista)  # dividindo a soma dos imcs pela quantidade de pacientes descobrimos a média destes.
print(f"A faixa de IMC está entre {max(tot_imc)} e  {min(tot_imc)}.")  # utilizando a função min e max para descobrir o maior e o menor imc da lista criada para descobrir sua faixa.
print(f"O IMC médio dos pacientes é {media_imc}")
print(f"Os pacientes com maior risco de vida são:\n"
      f" - {lista[ind_menor][0]}; IMC {lista[ind_menor][5]}; {lista[ind_menor][3]} cardíaco; status de vit.: {lista[ind_menor][4]}\n"
      f" - {lista[ind_maior][0]}; IMC {lista[ind_maior][5]}; {lista[ind_maior][3]} cardíaco; status de vit.: {lista[ind_maior][4]}")


# Busca a ficha de qualquer paciente desejado:
while True:
    cod = input("Digite o código do paciente que você quer analisar: ")
    if str(cod) in 'Bb':  # Break se o usuário digitar B ou b
        break
    print(df.iloc[int(cod)])

