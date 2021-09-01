import numpy as np
import pandas as pd

np.random.seed(101)

df = pd.DataFrame(np.random.randn(5, 4), index='A B C D E'.split(), columns=' W X Y Z'.split())

print(df)

print('=-' * 20)

print(df['Y'])  # Exibe 1 coluna
print(df[['X', 'Z']])  # Exibe 2 ou mais colunas

print('<>' * 20)
print(df)
df['new'] = df['W'] + df['X']  # Cria uma nova coluna
print(df)
df = df.drop('new', axis=1)  # Exclui uma coluna. Necessácio atribuir
print('-+' * 20)
print(df)
df.drop('Z', axis=1, inplace=True)  # Exclui uma coluna. Sem precisar atribuir
print(df)
df.drop('C', axis=0, inplace=True)
print(df)

print('=-' * 20)

np.random.seed(101)
df = pd.DataFrame(np.random.randn(5, 4), index='A B C D E'.split(), columns=' W X Y Z'.split())
print(df)
print(df.loc['D'])  # Exibe um índice
print(df.loc['C', 'X'])  # Exibe o valor de um índice e uma coluna
print(df.loc[['A', 'B'], ['X', 'Y', 'Z']])  # Exibe varios indices e colunas
print(df.iloc[1:4, 2:])  # Exibe índices e colunas na conotação de Numpy, ou seja, pela ordenação
