import numpy as np
import pandas as pd

d = {'A': [1,2, np.nan], 'B': [5, np.nan, np.nan], 'C': [1, 2, 3]}

df = pd.DataFrame(d)

print(df)
print('*=' * 20)
print(df.dropna())  # Exclui os índices que tenham pelo menos 1 valor faltando
print('*=' * 20)
print(df.dropna(axis=1))  # Exclui as colunas que tenham pelo menos 1 valor faltando
print('-=' * 20)
print(df.dropna(thresh=2))  # Exclui os índices com valor faltando. Exceto onde tenha pelo menos 2 valores normais

print('\033[1;35m*=\033[m' * 20)
print(df)
print('\033[1;35m*=\033[m' * 20)

print(df.fillna(value= 0))  # Peenche os valores vazios por 0
print('-=' * 20)
print(df['A'].fillna(df['A'].mean()))  # Preenche os vazios de A com a média de A
print('-=' * 20)
print(df.fillna(method='ffill'))  # Preenche os valores vazios pelo último valor preenchido antes dele na coluna