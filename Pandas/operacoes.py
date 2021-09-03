import pandas as pd
import numpy as np
df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})
df.head()

print(df['col2'].unique())  # Exibe os valores distintos contidos em col2
print(df['col2'].nunique())  # Exibe a qnt de valores distintos contidos em col2
print(df['col2'].value_counts())  # Exibe cada valor distinto e seu nº de incidências
print('=-' * 20)
print(df[df['col1'] > 2])  # Exibe as linhas onde col1 > 2
print('-' * 40)
print(df[(df['col1'] > 2) & (df['col2'] == 444)])  # Exibe as linhas onde col1 > 2 e col2 seja igual a 444

print('\033[1;35m=*\033[m' * 20)
print(df.sum())  # Retorna o somatório/concatenação dos elementos das colunas do DF
print('\033[1;35m=*\033[m' * 20)

def vezes2(x):  # Função que multiplica por 2
    return x * 2

print(df['col1'].apply(vezes2))  # Aplica uma função a cada elemento da coluna
print(df.apply(vezes2))  # Aplica uma função a cada elemento do Dataframe
print('-' * 40)
print(df['col1'].apply(lambda x : x * x))  # Usando apply com função lambda

print('\033[1;33m=*\033[m' * 20)
print(df)
del df['col2']  # Deleta uma coluna
print(df)
df['col4'] = [5, 7, 6, 2]  # Acrescenta uma coluna
print(df)
print('-' * 40)
print(df.columns)  # Exibe os nomes das colunas
print(df.index)  # Exibe os nomes dos índices
print(df.sort_values(by='col4'))  # Ordena os índices pelos valores de uma coluna
print('\033[1;36m=*\033[m' * 20)
print(df.isnull())  # Exibe em booleano os valores nulos
print('\033[1;37m=*\033[m' * 20)
data = {'A':['foo','foo','foo','bar','bar','bar'],
     'B':['one','one','two','two','one','one'],
       'C':['x','y','x','y','x','y'],
       'D':[1,3,2,5,4,1]}

df2 = pd.DataFrame(data)

print(df2)
print('-' * 40)
print(df2.pivot_table(values='D', index='A', columns='C'))

print(df2.head())




