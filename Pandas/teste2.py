import numpy as np
import pandas as pd

estados = ['MG', 'MG', 'MG', 'SP', 'SP', 'SP', 'ES', 'ES', 'ES']
cidades = ['Caratinga', 'Ipatinga', 'Timóteo', 'Sorocaba', 'Diadema', 'Piracicaba', 'Vila Velha', 'Vitória', 'Guarapari']
dados = [[1848, 92603], [1964, 265409], [1964, 90568], [1654, 687357], [1959, 426757], [1767, 407252], [1535, 501325], [1551, 365855], [1860, 126701]]

multindex = list(zip(estados, cidades))
multindex = pd.MultiIndex.from_tuples(multindex)

df = pd.DataFrame(dados, multindex, ['Fundação', 'População'])

print(df)