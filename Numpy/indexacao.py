
import numpy as np

arr = np.arange(50).reshape(5, 10)

print(arr)
print('=*' * 20 )
arr2 = []
for i in range(0,5):  # Fazendo dice sem Numpy
    aux = arr[i][3:5].copy()
    arr2.append(aux)
    print(arr[i][3:5])
print(arr[:, 3:6])  # Fazendo dice com Numpy

print('=-' * 20)

trios = arr %3 == 0  # Tabela trios Guarda True/False onde é divisível por 3
print(trios)  # Tabela com True e False
print("==" * 20)
print(arr[trios])  # Exibe apenas os elemento do array que forem True para trios

print('=*' *20)

arr3 = np.arange(1, 11)
print(arr3)
print(np.exp(arr3))  # Número de Euler (apx 2.718281)
