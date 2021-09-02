import pandas as pd

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']},
                   index=[0, 1, 2, 3])

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7']},
                   index=[4, 5, 6, 7])

df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                    'B': ['B8', 'B9', 'B10', 'B11'],
                    'C': ['C8', 'C9', 'C10', 'C11'],
                    'D': ['D8', 'D9', 'D10', 'D11']},
                   index=[8, 9, 10, 11])

print(df1)
print('-' * 40)
print(df2)
print('-' * 40)
print(df3)
print('*=' * 20)
print(pd.concat([df1, df2, df3]))  # Concatenando pelas colunas
print('*=' * 20)
print(pd.concat([df1, df2, df3], axis=1))  # Concatenando pelas linhas, não é muito aconselhável neste caso
# Deve-se atentar para a quantidade de linhas e colunas dos dataframes concatenados
print('\033[1;35m*=\033[m' * 20)

esquerda = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                         'A': ['A0', 'A1', 'A2', 'A3'],
                         'B': ['B0', 'B1', 'B2', 'B3']})

direita = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                        'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']})
print(esquerda)
print(direita)
print(pd.merge(esquerda, direita, how='inner', on='key'))  # Vai mesclar as tabelas com base na coluna key

print('\033[1;36m*=\033[m' * 20)
esquerda = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                         'key2': ['K0', 'K1', 'K0', 'K1'],
                         'A': ['A0', 'A1', 'A2', 'A3'],
                         'B': ['B0', 'B1', 'B2', 'B3']})

direita = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                        'key2': ['K0', 'K0', 'K0', 'K0'],
                        'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']})
print(direita)
print(esquerda)
print(pd.merge(esquerda, direita, on=['key1', 'key2']))  # Vai mostrar onde tem par em comum, K0K0 e K1K1
print('\033[1;32m*=\033[m' * 20)

esquerda = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                         'B': ['B0', 'B1', 'B2']},
                        index=['K0', 'K1', 'K2'])

direita = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                        'D': ['D0', 'D2', 'D3']},
                       index=['K0', 'K2', 'K3'])

print(esquerda)
print(direita)
print(esquerda.join(direita))  # Vai inderir o df direita onde tenha índice em comum com esquerda
print('-' * 20)
print(esquerda.join(direita, how='outer'))  # Vai inserir o df direita em esquerda

