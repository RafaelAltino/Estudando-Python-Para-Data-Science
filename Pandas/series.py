import numpy as np
import pandas as pd

labels = ['a', 'b', 'c']
minha_lista = [10, 20, 30]
arr = np.array([10, 20, 30])
d = {'a': 10, 'b': 20, 'c': 30}
matriz = np.arange(1, 10).reshape(3, 3)

print(labels)
print(minha_lista)
print(arr)
print(d)
print(matriz)
print('=*' * 20)

ser = pd.Series(data=minha_lista, index=labels)
print(ser)
print(ser['b'])

print('=*' * 20)

ser1 = pd.Series([1, 2, 3, 4], ['Alemanha', 'Brasil', 'Canadá', 'Dinamarca'])
ser2 = pd.Series([1, 2, 3, 4], ['Alemanha', 'Brasil', 'Croácia', 'Dinamarca'])

print(ser1)
print('-'* 5)
print(ser2)
print('*' * 10)
print(ser1 + ser2)


