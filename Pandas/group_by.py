import pandas as pd

# Cria um DataFrame
data = {'Empresa':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
       'Nome':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
       'Venda':[200,120,340,124,243,350]}

df = pd.DataFrame(data)
print(df)
print('*=' * 20)
group = df.groupby('Empresa')  # Agrupa os dados por empresa

print(group)
print('*=' * 20)
print(group.sum())  # Somatorio dos valores por empresa
print('*=' * 20)
print(group.describe())  # Descrição dos itens por empresa
print('*=' * 20)
print(group.count())  # Contagem dos itens de cada empresa
print('\033[1;35m*=\033[m' * 20)
group2 = df.groupby('Nome')  # Agrupando por nome agora
print(group2.sum())  # Somatório dos valores por cada nome
print('*=' * 20)
print(group2.sum().loc['Amy'])  # Somatório dos valores (vendas) da Amy

