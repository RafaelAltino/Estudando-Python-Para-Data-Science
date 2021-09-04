import numpy as np
import pandas as pd

df = pd.read_csv('exemplo', sep=',', decimal='.')  # Importa a base exemplo
# Os parâmetros sep e decimal são opcionais, mas servem para indicar
# Quais serão os separadores dos valores e das casas decimais.

print(df)

df += 1

print(df)

df.to_csv("exemplo.csv", sep=';', decimal=',')  # Exporta o dataframe para um csv

print('\033[1;35m=*\033[m' * 20)

# df2 = pd.read_excel('Tabela Pokemon.xlsx', sheet_name='Planilha1')  # Importa um arquivo de excel

# print(df2)

# df2.to_excel('pkmexportado.xlsx', sheet_name='Alola')  # Exporta o dataframe para um arquivo excel .xlsx

print('\033[1;32m=*\033[m' * 20)

df3 = pd.read_html('https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/')  # Importa uma tabela de uma página html
#  Vai retornar uma lista, e a tabela que você quer pode estar em alguma posição da lista
#  Como por exemplo, neste caso a tabela que eu quero está na posicão 0 do meu df
print(df3[0].columns)
print(df3[0])