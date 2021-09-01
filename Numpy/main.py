import numpy as np

minha_lista = [1, 2, 3]

minha_matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(minha_lista)

print(np.array(minha_lista))  # Exibe o array de forma simplificada
print(np.array(minha_matriz))  # Exibe a matriz de forma simplificada

print('=-' * 20)

print(np.arange(0, 10))  # Preenche um vetor de 0 a 9
print(np.arange(0, 10, 3))  # Preenche um vetor de 0 a 9 pulando de 3 em 3

print('=-' * 20)

print(np.zeros(5))  # Preenche um vetor de 5 casas com zeros
print(np.zeros((2, 3)))  # Preenche uma matriz de 2 linhas e 3 colunas com zeros

print('=-' * 20)

print(np.ones(3))  # Preenche um vetor de 5 casas com uns
print(np.ones((2, 3)))  # Preenche uma matriz de 2 linhas e 3 colunas com uns
print(np.eye(4))  # Cria uma matriz identidade de 4 por 4. Diagonal principal preenchida por 1 e demais por 0

print('=-' * 20)

print(np.linspace(0, 24, 5))  # Cria um vetor de 5 espaços preenchidos por intervalos de 0 a 24
print(np.linspace(0, 24, 3))  # Cria um vetor de 3 espaços preenchidos por intervalos de 0 a 24

print('=-' * 20)

print(np.random.rand(5))  # Vetor de 5 casas preenchidas por valores aleatórios entre 0 e 1. Distibuição uniforme
print(np.random.rand(2, 3))  # Matriz 2 por 3 preenchida por valores aleatórios entre 0 e 1. Distribuição uniforme

print('=-' * 20)

print(np.random.rand(5))  # Distribuição uniforme
print(np.random.randn(5))  # Distribuição Normal/Gaussiana (média 0, desvio padrão 1)
print(np.random.randint(0, 100, 10))  # Cria um Vetor de 10 valores aleatorios  de 0-99

print('=-' * 20)

arr = np.random.rand(25)  # Cria vetor de 25 casas
print(arr)
print(arr.reshape(5, 5))  # Retorna o vetor como matrix de 5 por 5

print('=-' * 20)

teste = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])  # Criei um vetor de 9 posições
print(teste.reshape(3,3))  # Re-arrumei ele para uma matriz 3 por 3

print(teste.shape)  # Mostra o numero de dimensoes da matriz/vetor
print(arr.max())  # Mostra o maior valor
print(arr.min())  # Mostra o menor valor
print(arr.argmax())  # Mostra a posição do maior valor
print(arr.argmin())  # Mostra a posição do menor valor
