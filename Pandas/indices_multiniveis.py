import numpy as np
import pandas as pd

outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1, 2, 3, 1, 2, 3]
hier_index = list(zip(outside, inside))  # Junta as listas combinando-as
print(hier_index, '\n')
hier_index = pd.MultiIndex.from_tuples(hier_index)  # Transforma um um MultIndex
print(hier_index, '\n')

# Passa o MultIndex como índice, ele serve como categorias e subcategorias
# Ex: [MG(Caratinga, Ipatinga, BH), ES(Vila Velha, Vitória, Guarapari), SP(...)]
df = pd.DataFrame(np.random.randn(6, 2), index=hier_index, columns= ['A', 'B'])

print(df)

print('*=' * 20)

print(df.loc['G1'].loc[1])  # Exibe os itens no: indice G1, indice 1

df.index.names = ['Grupo', 'Numero']

print(df)

print(df.xs('G1'))

print(df.xs(1, level='Numero'))