import numpy as np
import pandas as pd
from numpy.random import randn
np.random.seed(101)

df = pd.DataFrame(randn(5, 4), index='A B C D E'.split(), columns='W X Y Z'.split())

print(df)

print('=-' * 20)

bol = df > 0
print(df[bol])
print('--' * 20)
print(df[df['W'] > 0])  # Exibe por completo o dataframe, exceto as linhas onde W < 0
print(df[df['W'] > 0]['Y'])  # Este comando exibe os itens de Y que atendam a condição

print('=-*+' * 20)
print(df[df['W'] > 0])
print(df[df['W'] > 0]['Y'])  # Este comando exibe os itens de Y que atendam a condição
"""  # O comando acima equivale a estes 3 comando abaixo
bol = df['W'] > 0
df2 = df[bol]
print(df2['Y'])
"""

print('=-'  * 20)

print(df[(df['W'] > 0) & (df['Y'] > 1)])  # Exibe onde atenda a estas 2 condições

print('=-'  * 20)

df.reset_index(inplace=True)  # Reseta o índex para o padrão (0, 1, 2, 3, ...)
print(df)  # O índice anterior se torna uma nova coluna

print('*=' * 20)

col = 'RJ SP MG ES GO'.split()
df['Estado'] = col
print(df)
df.set_index('Estado', inplace=True)  # Substitui o índice pela lista de Estados
print(df)