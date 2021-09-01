import numpy as np
import pandas as pd
maior = 10
amostras = 100  # Deve ser número com raiz quadrada exata
tamanho = round(np.sqrt(amostras))

matriz = np.random.randint(0, maior, amostras).reshape(tamanho, tamanho)
print(matriz)

contagem = pd.Series(np.zeros(maior), [np.arange(0, maior)])

for i in range(0, maior):
    contagem[i] = len(matriz[matriz == i])

print(contagem)
print(contagem.sum())
